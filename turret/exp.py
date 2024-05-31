import cv2
import requests
import time
import serial  # Import the serial library

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
server_url = "http://10.12.13.50:8080"
arduino_serial_port = "COM6"  # Replace with the correct serial port of your Arduino

request_delay = 0.1  # Adjust this value as needed

# Open serial port to Arduino
arduino_serial = serial.Serial(arduino_serial_port, 9600, timeout=1.0)
time.sleep(1)

def send_coordinates(x, y):
    coordinates = "X{}Y{}".format(x, y)
    payload = {'coordinates': coordinates}

    try:
        # Send coordinates to NodeMCU server
        response = requests.post(f"{server_url}/set_coordinates", data=payload)
        if response.status_code == 200:
            print("Coordinates sent successfully to NodeMCU")
            print(f"Sent coordinates: ({x}, {y})")
        else:
            print(f"Error sending coordinates to NodeMCU. Status code: {response.status_code}")

        # Send coordinates to Arduino over serial
        arduino_serial.write(coordinates.encode('ascii'))
    except requests.exceptions.RequestException as e:
        print(f"Error sending coordinates: {e}")

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # mirror the image

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)  # detect the face

    for x, y, w, h in faces:
        # Sending coordinates to the server
        x_coord = 640 - (x + w // 2)  # Reversing the X-coordinate
        y_coord = y + h // 2

        send_coordinates(x_coord, y_coord)

        # Plot the center of the face
        cv2.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
        # Plot the ROI
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Plot the squared region in the center of the screen
    cv2.rectangle(frame, (640 // 2 - 30, 480 // 2 - 30),
                  (640 // 2 + 30, 480 // 2 + 30),
                  (255, 255, 255), 3)

    cv2.imshow('img', frame)

    # Press 'q' to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    time.sleep(request_delay)  # Add a delay between consecutive requests

# Close serial port
arduino_serial.close()
cap.release()
cv2.destroyAllWindows()
