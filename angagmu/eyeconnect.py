import cv2
import numpy as np
import pyautogui
import time
import threading
import tkinter as tk
pyautogui.FAILSAFE=False
# Global variables for eye tracking
eye_position = (0, 0)  # Initial eye position (x, y)
screen_width, screen_height = pyautogui.size()  # Get screen size
smooth_factor = 0.1  # Smoothing factor for cursor movement
zoom_factor = 3  # Factor to zoom into the eye region

# Global variables for word picking
selected_word = ""  # Store the selected word
stable_eye_position = None  # Keep track of stable eye position for better accuracy

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
    global selected_word

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

        # Check which word is under the cursor and update selected_word
        if new_x < 400:  # Assuming left word is on the left half
            selected_word = "Help"
        elif new_x > 600:  # Assuming right word is on the right half
            selected_word = "Play"
        elif new_y < 300:  # Assuming top word is at the top
            selected_word = "Hungry"
        elif new_y > 400:  # Assuming bottom word is at the bottom
            selected_word = "Bathroom"
        else:
            selected_word = ""

        # Add a small delay to control speed
        time.sleep(0.05)  # Increase this delay if it's still too fast

# Function to track stable eye position
def stable_eye_position_tracking():
    global stable_eye_position
    global eye_position

    previous_position = None
    count = 0

    while True:
        if eye_position == previous_position:
            count += 1
        else:
            count = 0

        # Confirm the position only after it stays stable for a few frames
        if count >= 5:  # Adjust sensitivity by changing this value
            stable_eye_position = eye_position

        previous_position = eye_position
        time.sleep(0.1)  # Slight delay to reduce rapid changes

# Function to create the word picker interface
def create_word_picker():
    global selected_word, stable_eye_position

    # Tkinter window setup
    root = tk.Tk()
    root.title("Eye-Tracking Word Picker")
    root.geometry("800x600")

    # Display widget to show the selected word
    selected_label = tk.Label(root, text="Selected Word:", font=("Arial", 24))
    selected_label.pack(pady=10)

    word_display = tk.Label(root, text="", font=("Arial", 24))
    word_display.pack()

    # Words mapped to four positions
    words = {
        "Left": "Help",
        "Right": "Play",
        "Top": "Hungry",
        "Bottom": "Bathroom"
    }

    # Create labels for words at their positions
    labels = {
        "Left": tk.Label(root, text="Help", font=("Arial",30)),
        "Right": tk.Label(root, text="Play", font=("Arial", 30)),
        "Top": tk.Label(root, text="Hungry", font=("Arial", 30)),
        "Bottom": tk.Label(root, text="Bathroom", font=("Arial", 30)),
    }

    # Position words on the screen
    labels["Left"].place(x=50, y=250)
    labels["Right"].place(x=650, y=250)
    labels["Top"].place(x=350, y=50)
    labels["Bottom"].place(x=350, y=450)

    # Function to highlight and display the selected word
    def highlight_and_display():
        global stable_eye_position

        while True:
            word_display.config(text=f"Selected: {selected_word}")  # Update the display with the current selected word
            word_display.update()
            time.sleep(0.1)  # Refresh rate for selected word display

    # Run word selection logic in a separate thread
    threading.Thread(target=highlight_and_display, daemon=True).start()

    root.mainloop()

# Main program to start eye detection, stable eye tracking, and word picker
if __name__ == "__main__":
    # Start eye detection and stable eye tracking in separate threads
    eye_thread = threading.Thread(target=detect_eye)
    eye_thread.daemon = True
    eye_thread.start()

    stable_eye_thread = threading.Thread(target=stable_eye_position_tracking)
    stable_eye_thread.daemon = True
    stable_eye_thread.start()

    # Start the cursor movement logic
    move_cursor_thread = threading.Thread(target=move_cursor_smoothly)
    move_cursor_thread.daemon = True
    move_cursor_thread.start()

    # Launch the word picker interface
    create_word_picker()
