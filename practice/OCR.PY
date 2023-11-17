# Importing necessary libraries
import cv2
import pytesseract
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import glob

# Setting up Tesseract path (modify according to your Tesseract installation)
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract.exe'  # Update this path

# Function to preprocess the image
def preprocess_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return adaptive_thresh

# Function to extract text using Tesseract
def extract_text_from_image(image):
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(processed_image)

    return extracted_text

# Function to display the image
def display_image(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# Function to handle a single image
def process_single_image(image_path):
    # Display the image
    print("\nProcessing Image: ", image_path)
    display_image(image_path)

    # Extract text
    extracted_text = extract_text_from_image(image_path)

    # Print the extracted text
    print("\nExtracted Text:")
    print(extracted_text)

# Function to process multiple images in a directory
def process_multiple_images(directory_path):
    # Get all image paths
    image_paths = glob.glob(os.path.join(directory_path, "*.jpg"))

    for image_path in image_paths:
        process_single_image(image_path)

# Function to check if path is a file or directory
def is_directory(path):
    return os.path.isdir(path)

# Main function to process an image or multiple images in a directory
def main(path):
    if is_directory(path):
        process_multiple_images(path)
    else:
        process_single_image(path)

# Example usage
path = 'path/to/your/image_or_directory'  # Update this path
main(path)
