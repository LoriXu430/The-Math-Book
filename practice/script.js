function performOCR() {
  const imageInput = document.getElementById('image-input');
  const outputParagraph = document.getElementById('output');

  if (imageInput.files && imageInput.files[0]) {
    const reader = new FileReader();

    reader.onload = function (e) {
      Tesseract.recognize(
        e.target.result,
        'eng', // You can change the language code if needed
        {
          logger: m => console.log(m) // Logs progress
        }
      ).then(({ data: { text } }) => {
        outputParagraph.textContent = text;
      });
    }

    reader.readAsDataURL(imageInput.files[0]);
  } else {
    alert('Please select an image file.');
  }
}
