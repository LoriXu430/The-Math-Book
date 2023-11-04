from flask import Flask, request, render_template, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

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
        image = Image.open(image_stream)

        try:
            text = pytesseract.image_to_string(image, lang='eng')  # Use 'eng+<your-language-code>' for multilingual support
            return jsonify({'text': text}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
