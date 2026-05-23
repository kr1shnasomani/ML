<h1 align="center">FaceCapture</h1>

Detects faces in an image, draws bounding boxes, and generates a grid of cropped faces.

## Approach
- **Face Detection**: Haar cascade classifier via OpenCV.
- **Processing**: Extracts and resizes detected faces into a structured grid.

## Performance
Fast, real-time capable detection for standard images.

## Installation & Execution
```bash
cd FaceCapture
pip install -r requirements.txt
python code/main.py
```
