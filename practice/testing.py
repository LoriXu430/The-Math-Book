# Test OCR with various images
# Conduct tests with low-resolution and noisy background images
# Experiment with batch processing of images

import pytesseract

def perform_ocr(image_path):
    text = pytesseract.image_to_string(image_path)
    return text

# Test OCR with different images
image_paths = ['image1.png', 'image2.jpg', 'image3.png']
for image_path in image_paths:
    text = perform_ocr(image_path)
    print(f"OCR Output for {image_path}:")
    print(text)
