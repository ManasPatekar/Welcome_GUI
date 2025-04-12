import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

# Get the correct path whether running as script or .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller adds this when running .exe
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Create the main window
root = tk.Tk()
root.title("Welcome!")
root.geometry("800x500")
root.resizable(False, False)

# Load and display background image
bg_path = resource_path("bg2.png")
bg_image = Image.open(bg_path)
bg_image = bg_image.resize((800, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Text content
welcome_text = canvas.create_text(400, 100, text="💻 Welcome to Your PC 💻",
                                   font=("Courier New", 28, "bold"),
                                   fill="white", state='hidden')

quote_text = canvas.create_text(400, 300,
    text='“A goal without a plan is just a wish.”',
    font=("Times New Roman", 16, "italic"), fill="white", justify="center", state='hidden')


# Fade-in animation
def fade_in(text_item, delay=50, steps=10):
    for i in range(steps + 1):
        alpha = int(255 * i / steps)
        hex_color = f"#{alpha:02x}{alpha:02x}{alpha:02x}"
        canvas.itemconfig(text_item, fill=hex_color)
        canvas.update()
        root.after(delay)

def show_motion():
    canvas.itemconfig(welcome_text, state='normal')
    fade_in(welcome_text)
    canvas.itemconfig(quote_text, state='normal')
    fade_in(quote_text)

# Call motion after slight delay
root.after(500, show_motion)

# Close after 8 seconds
root.after(8000, root.destroy)

root.mainloop()
