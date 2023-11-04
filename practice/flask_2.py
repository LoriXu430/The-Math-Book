from flask import Flask, request, render_template, jsonify
import pytesseract
from PIL import Image, ImageFilter
import io
import threading
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

def preprocess_image(image):
    """
    Apply image preprocessing to improve OCR results.
    """
    # Example preprocessing: converting to grayscale
    image = image.convert('L')
    image = image.filter(ImageFilter.SHARPEN)
    return image

def async_ocr(image_stream, callback):
    """
    Perform OCR asynchronously and call the provided callback with the result.
    """
    def run_ocr():
        try:
            image = Image.open(image_stream)
            image = preprocess_image(image)
            text = pytesseract.image_to_string(image, lang='eng')
            callback({'text': text}, 200)
        except Exception as e:
            callback({'error': str(e)}, 500)

    thread = threading.Thread(target=run_ocr)
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')  # You would create this template

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image_stream = io.BytesIO(file.read())
        image_stream.seek(0)

        def on_ocr_complete(result, status_code):
            # This function will be called when OCR is complete
            app.logger.info('OCR complete')
            return jsonify(result), status_code

        async_ocr(image_stream, on_ocr_complete)
        return jsonify({'message': 'OCR started'}), 202
    else:
        return jsonify({'error': 'Invalid file'}), 400

if __name__ == '__main__':
    app.run(debug=True)
