<h1 align="center">FaceCapture</h1>
This script detects faces in an image using a Haar cascade classifier, draws bounding boxes around detected faces, saves the result, and generates a grid of cropped, resized faces using Matplotlib. It handles multiple faces and saves outputs to specified paths.

## Execution Guide:
1. Clone the repository:
   ```
   git clone https://github.com/kr1shnasomani/Facetronix.git
   cd Facetronix/FaceFeel
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Upon running the code it will detect the faces and save two files - `boundingbox.jpg` and `croppedface.jpg`

## Result:

   Input Image:

   ![image](https://github.com/user-attachments/assets/e0689480-34ab-40bb-ba8b-a16ce25b1112)

   Output Image:

   a. `boundingbox.jpg`

   ![boundingbox](https://github.com/user-attachments/assets/bbc0cc97-bae5-47f9-964f-57a7cc080420)

   b. `croppedface.jpg`

   ![croppedface](https://github.com/user-attachments/assets/5f0a3434-e4b6-442e-be18-36e471931c8d)
