import cv2
import numpy as np
import sys
import tkinter as tk
from tkinter import filedialog, Scale

def update_parameters():
    blur_ksize = blur_ksize_scale.get() * 2 + 1
    blur_sigma = blur_sigma_scale.get()
    log_ksize = log_ksize_scale.get() * 2 + 1
    threshold = threshold_scale.get()
    block_size = block_size_scale.get() * 2 + 3

    blurred_image = cv2.GaussianBlur(image_gray, (blur_ksize, blur_ksize), blur_sigma)
    log_image = cv2.Laplacian(blurred_image, cv2.CV_32F, ksize=log_ksize)
    log_image = cv2.convertScaleAbs(log_image)  # Convert the data type to uint8
    _, thresholded_image = cv2.threshold(log_image, threshold, 255, cv2.THRESH_BINARY_INV)

    adaptive_threshold = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, 2)
    combined_image = cv2.bitwise_and(thresholded_image, adaptive_threshold)

    cv2.imshow('Enhanced Edges', combined_image)

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
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image_gray is None:
        print("Error: Image not found.")
        sys.exit(1)

    # Create a Tkinter window for sliders
    sliders_window = tk.Tk()
    sliders_window.title("Adjust Parameters")

    # Create sliders
    blur_ksize_scale = Scale(sliders_window, from_=1, to=15, label="Gaussian blur ksize", command=lambda x: update_parameters())
    blur_ksize_scale.set(2)
    blur_ksize_scale.pack()
    blur_sigma_scale = Scale(sliders_window, from_=1, to=20, label="Gaussian blur sigma", command=lambda x: update_parameters())
    blur_sigma_scale.set(5)
    blur_sigma_scale.pack()
    log_ksize_scale = Scale(sliders_window, from_=1, to=15, label="Laplacian ksize", command=lambda x: update_parameters())
    log_ksize_scale.set(2)
    log_ksize_scale.pack()
    threshold_scale = Scale(sliders_window, from_=1, to=255, label="Threshold", command=lambda x: update_parameters())
    threshold_scale.set(50)
    threshold_scale.pack()
    block_size_scale = Scale(sliders_window, from_=1, to=15, label="Adaptive Threshold block size", command=lambda x: update_parameters())
    block_size_scale.set(4)
    block_size_scale.pack()

    # Initial display
    update_parameters()

    # Start the Tkinter main loop
    sliders_window.mainloop()

    # Close the OpenCV window
    cv2.destroyAllWindows()
