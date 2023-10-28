const puppeteer = require('puppeteer');
const path = require('path');

describe('OCR Functionality', () => {
  let browser;
  let page;

  beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
    await page.goto('http://localhost:3000'); // Change to your actual web app URL
  });

  afterAll(async () => {
    await browser.close();
  });

  test('should recognize text from image', async () => {
    const imagePath = path.resolve(__dirname, './path/to/your/test-image.png');
    const expectedText = 'This is a sample text';

    // Upload the image
    const fileInput = await page.$('#image-input');
    await fileInput.uploadFile(imagePath);

    // Click the "Recognize Text" button
    await page.click('button');

    // Wait for OCR to complete and get the recognized text
    const recognizedText = await page.$eval('#output', el => el.textContent);

    // Verify the recognized text
    expect(recognizedText).toContain(expectedText);
  });
});
