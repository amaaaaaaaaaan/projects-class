import cv2
import numpy as np
import pyautogui
import time
import threading
pyautogui.FAILSAFE=False
# Global variables
eye_position = (0, 0)  # Initial eye position (x, y)
screen_width, screen_height = pyautogui.size()  # Get screen size
smooth_factor = 0.1  # Smoothing factor for cursor movement
zoom_factor = 3  # Factor to zoom into the eye region

# Function to interpolate between current position and target position
def lerp(start, end, factor):
    return start + (end - start) * factor

# Function to detect eye movement and calculate the eye coordinates
def detect_eye():
    global eye_position

    cap = cv2.VideoCapture(0)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally to mirror the video feed
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        if len(eyes) > 0:
            # Take the first detected eye for simplicity
            (ex, ey, ew, eh) = eyes[0]

            # Extract the eye region
            eye_region = gray[ey:ey + eh, ex:ex + ew]
            eye_region_color = frame[ey:ey + eh, ex:ex + ew]  # Color eye region for visualization

            # Zoom into the eye region
            height, width = eye_region.shape
            zoomed_eye_region = cv2.resize(eye_region, (width * zoom_factor, height * zoom_factor))

            # Threshold the zoomed eye region to find the pupil
            _, thresholded_eye = cv2.threshold(zoomed_eye_region, 60, 255, cv2.THRESH_BINARY_INV)

            # Find contours of the thresholded image
            contours, _ = cv2.findContours(thresholded_eye, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                # Find the largest contour, which should be the pupil
                largest_contour = max(contours, key=cv2.contourArea)

                # Get the coordinates of the bounding box around the pupil
                (px, py, pw, ph) = cv2.boundingRect(largest_contour)

                # Calculate the pupil center relative to the original frame
                pupil_center_x = ex + (px + pw // 2) * zoom_factor
                pupil_center_y = ey + (py + ph // 2) * zoom_factor

                # Update the global eye_position
                eye_position = (pupil_center_x, pupil_center_y)

                # Draw a circle around the pupil for visualization
                cv2.circle(eye_region_color, (px + pw // 2, py + ph // 2), 5, (0, 255, 0), -1)

            # Optional: Draw a rectangle around the detected eye
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

            # Show the zoomed eye region for debugging
            cv2.imshow("Zoomed Eye Region", zoomed_eye_region)

        # Display the flipped frame
        cv2.imshow("Eye Tracker", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to move the cursor smoothly to the target position
def move_cursor_smoothly():
    current_position = pyautogui.position()  # Start at the current cursor position

    while True:
        target_position = eye_position

        # Use linear interpolation (LERP) for smooth movement
        new_x = int(lerp(current_position[0], target_position[0], smooth_factor))
        new_y = int(lerp(current_position[1], target_position[1], smooth_factor))

        # Move the cursor to the new position
        pyautogui.moveTo(new_x, new_y)

        # Update current position for the next iteration
        current_position = (new_x, new_y)

        # Add a small delay to control speed
        time.sleep(0.05)  # Increase this delay if it's still too fast

# Main program
if __name__ == "__main__":
    # Start eye detection in a separate thread
    eye_thread = threading.Thread(target=detect_eye)
    eye_thread.daemon = True
    eye_thread.start()

    # Start the cursor movement logic
    move_cursor_smoothly()




