# 🐱 Cat Face Detection API using FastAPI

This project is a simple API built with **FastAPI**, **OpenCV**, and **NumPy** to detect cat faces in an uploaded image and return the image with bounding boxes around the detected faces.

---

## 📦 Requirements

Install the required dependencies using:

```bash
pip install fastapi uvicorn opencv-python numpy

> The io module is built into Python and does not need to be installed.




---

🚀 Running the Server

Start the FastAPI server with:

uvicorn main:app --reload

> Replace main with your actual Python file name if it's different.




---

📤 API Endpoint

POST /object_detection

Request:

Accepts an image file (JPEG, PNG, etc.) uploaded as form-data with the key: input_file.

Example using curl:

curl -X POST "http://127.0.0.1:8000/object_detection" \
  -H "accept: image/jpeg" \
  -H "Content-Type: multipart/form-data" \
  -F "input_file=@cat.jpg" --output result.jpg


---

⚙️ How It Works

1. Receives an image file from the client.


2. Checks if the uploaded file is an image.


3. Reads and decodes the image using NumPy and OpenCV.


4. Detects cat faces using OpenCV’s Haar cascade:
haarcascade_frontalcatface.xml


5. Draws green rectangles around the detected faces.


6. Returns the processed image as a JPEG file.




---

📂 Project Structure

project/
│
├── main.py # FastAPI app with the detection logic
├── README.md # This file


---

📸 Sample Output

Input: A cat image (cat.jpg)

Output: The same image with green boxes around detected cat faces (result.jpg)



---

⚠️ Notes

Make sure the Haar cascade XML file is properly loaded using:

cv2.data.haarcascades + "haarcascade_frontalcatface.xml"

For better accuracy, you can convert the image to grayscale before detection (optional and commented out in the code).



---

👨‍💻 Author

Developed by [Your Name]
Inspired by OpenCV object detection examples.


---

📄 License

This project is licensed under the MIT License.


---

✅ You can now copy this content into your README.md file.

Let me know if you'd like me to auto-generate a GitHub-style badge section or include a sample image display in Markdown.