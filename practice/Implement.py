# Example code for implementing OCR in a new language (using pytesseract)
import pytesseract

# Set the language for OCR (replace 'eng' with the language code for your target language)
language_code = 'fra'  # Example for French

# Perform OCR with the specified language
def perform_multilingual_ocr(image_path):
    text = pytesseract.image_to_string(image_path, lang=language_code)
    return text

# Test the multilingual OCR with sample images
image_paths = ['image1.png', 'image2.jpg', 'image3.png']
for image_path in image_paths:
    text = perform_multilingual_ocr(image_path)
    print(f"OCR Output for {image_path} in {language_code}:")
    print(text)

# Research and implement language-specific OCR challenges and best practices
