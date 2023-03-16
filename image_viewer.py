import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")

        # Create buttons for opening and closing images
        self.open_button = tk.Button(self.master, text="Open Image", command=self.open_image)
        self.open_button.pack(side="top", padx=10, pady=10)

        self.close_button = tk.Button(self.master, text="Close Image", command=self.close_image)
        self.close_button.pack(side="top", padx=10, pady=10)

        # Create canvas for displaying the image
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.image = None

    def open_image(self):
        # Determine which file dialog to use based on the platform
        if os.name == 'nt':  # Windows
            file_path = filedialog.askopenfilename()
        else:  # Linux or Mac
            file_path = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                                   filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))

        # If file path is not empty, open the image
        if file_path != '':
            # Load the image and resize it to fit the canvas
            self.image = Image.open(file_path)
            self.image = self.image.resize((500, 500), Image.ANTIALIAS)

            # Display the image on the canvas
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)

    def close_image(self):
        # Remove the image from the canvas and reset the image variable
        self.canvas.delete("all")
        self.image = None

if __name__ == '__main__':
    root = tk.Tk()
    ImageViewer(root)
    root.mainloop()
