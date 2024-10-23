import tkinter as tk

# Function to change the background color when hovering
def on_enter(event):
    event.widget.config(bg="lightblue")  # Change the background color when hovered

# Function to revert to original background color when leaving
def on_leave(event):
    event.widget.config(bg="SystemButtonFace")  # Reset to default background color

# Create the main window
root = tk.Tk()
root.title("Hover Button Example")
root.geometry("300x200")

# Create a button
hover_button = tk.Button(root, text="Hover over me", font=("Arial", 16), width=15)

# Bind the hover events to the button
hover_button.bind("<Enter>", on_enter)  # When the cursor enters the button area
hover_button.bind("<Leave>", on_leave)  # When the cursor leaves the button area

# Place the button in the window
hover_button.pack(pady=50)

# Run the main Tkinter loop
root.mainloop()
