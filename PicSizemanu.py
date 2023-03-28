import cv2
import numpy as np
import sys
import tkinter as tk
from tkinter import filedialog

scale_factor = 1.33  # Update the scale factor to convert pixel size to real size

def mouse_callback(event, x, y, flags, param):
    global image_color, drawing, center, radius, circles

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        center = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            image_copy = image_color.copy()
            radius = int(np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2))
            cv2.circle(image_copy, center, radius, (0, 255, 0), 2)
            display_circles(image_copy, circles)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(image_color, center, radius, (0, 255, 0), 2)
        circles.append((center, radius))

def display_circles(image, circles):
    image_copy = image.copy()
    for (center, radius) in circles:
        cv2.circle(image_copy, center, radius, (0, 255, 0), 2)

    mean_radius = np.mean([radius for (_, radius) in circles]) if circles else 0
    mean_diameter = 2 * mean_radius * scale_factor
    mean_diameter_text = f"Mean Diameter: {mean_diameter:.2f}"
    cv2.putText(image_copy, mean_diameter_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Calculate PDI
    radii = np.array([radius for (_, radius) in circles])
    pdi = np.square(np.std(radii)) / np.square(np.mean(radii)) if circles else 0
    pdi_text = f"PDI: {pdi:.2f}"
    cv2.putText(image_copy, pdi_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('Draw Circles', image_copy)

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp;*.tif")])
    return file_path

if __name__ == "__main__":
    # Select an image
    image_path = select_image()

    if not image_path:
        print("No image selected.")
        sys.exit(1)

    # Load the image
    image_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if image_color is None:
        print("Error: Image not found.")
        sys.exit(1)

    # Initialize drawing variables
    drawing = False
    center = (-1, -1)
    radius = 0
    circles = []

    # Create a window and set the callback functions for mouse events
    cv2.namedWindow('Draw Circles')
    cv2.setMouseCallback('Draw Circles', mouse_callback)
    display_circles(image_color, circles)

    # Wait for user input and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
