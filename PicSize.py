import cv2
import numpy as np
import sys
import tkinter as tk
from tkinter import filedialog, Scale

def detect_circles(image, dp=1, min_dist=20, param1=100, param2=30, min_radius=5, max_radius=0):
    # Preprocess the image
    blurred_image = cv2.medianBlur(image, 5)

    # Apply Hough Circle Transform
    circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp, min_dist, param1=param1, param2=param2,
                                minRadius=min_radius, maxRadius=max_radius)

    return circles

def calculate_mean_diameter(circles, line_length_nm, line_length_px):
    if circles is None:
        return None

    radii = [circle[2] for circle in circles[0, :]]
    diameters = [2 * radius for radius in radii]

    # Calculate the scaling factor
    scale_factor = line_length_nm / line_length_px

    # Convert the diameters to nanometers
    diameters_nm = [diameter * scale_factor for diameter in diameters]

    # Calculate the mean diameter
    mean_diameter_nm = np.mean(diameters_nm)
    return mean_diameter_nm

def display_circles(image, circles, line_length):
    # Create a copy of the original image to draw circles and the reference line on
    image_copy = image.copy()

    # Draw circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            x, y, radius = circle
            cv2.circle(image_copy, (x, y), radius, (0, 255, 0), 2)

    # Draw red horizontal reference line
    height, width, _ = image_copy.shape
    line_start = (25, height - 5)
    line_end = (25 + line_length, height - 5)
    cv2.line(image_copy, line_start, line_end, (0, 0, 255), 2)

    # Calculate and display the mean diameter
    mean_diameter_nm = calculate_mean_diameter(circles, 100, line_length)
    if mean_diameter_nm is not None:
        mean_diameter_text = f"Mean Diameter: {mean_diameter_nm:.2f} nm"
        cv2.putText(image_copy, mean_diameter_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Show the image
    cv2.imshow('Detected Circles', image_copy)

def update_parameters():
    dp = dp_scale.get()
    min_dist = min_dist_scale.get()
    param1 = param1_scale.get()
    param2 = param2_scale.get()
    min_radius = min_radius_scale.get()
    max_radius = max_radius_scale.get()
    line_length = line_length_scale.get()

    circles = detect_circles(image_gray, dp, min_dist, param1, param2, min_radius, max_radius)
    display_circles(image_color, circles, line_length)

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
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image_gray is None or image_color is None:
        print("Error: Image not found.")
        sys.exit(1)

    # Create a Tkinter window for sliders
    sliders_window = tk.Tk()
    sliders_window.title("Adjust Parameters")

    # Create sliders
    dp_scale = Scale(sliders_window, from_=1, to=10, label="dp", command=lambda x: update_parameters())
    dp_scale.pack()
    min_dist_scale = Scale(sliders_window, from_=1, to=100, label="min_dist", command=lambda x: update_parameters())
    min_dist_scale.set(20)
    min_dist_scale.pack()
    param1_scale = Scale(sliders_window, from_=1, to=300, label="param1", command=lambda x: update_parameters())
    param1_scale.set(100)
    param1_scale.pack()
    param2_scale = Scale(sliders_window, from_=1, to=100, label="param2", command=lambda x: update_parameters())
    param2_scale.set(30)
    param2_scale.pack()
    min_radius_scale = Scale(sliders_window, from_=1, to=100, label="min_radius", command=lambda x: update_parameters())
    min_radius_scale.set(5)
    min_radius_scale.pack()
    max_radius_scale = Scale(sliders_window, from_=0, to=500, label="max_radius", command=lambda x: update_parameters())
    max_radius_scale.set(50)
    max_radius_scale.pack()
    line_length_scale = Scale(sliders_window, from_=10, to=500, label="line_length", command=lambda x: update_parameters())
    line_length_scale.set(50)
    line_length_scale.pack()

    # Initial display
    update_parameters()

    # Start the Tkinter main loop
    sliders_window.mainloop()

    # Close the OpenCV window
    cv2.destroyAllWindows()
