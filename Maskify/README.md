<h1 align="center">Maskify</h1>
This script detects faces in an image using a Caffe model and predicts mask usage with a Keras classifier. It annotates faces with bounding boxes and labels ("Mask" or "No Mask") based on predictions, saving the annotated image to a specified path.

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

3. Download the following models:

   a. [deploy.prototxt](https://github.com/kr1shnasomani/Facetronix/blob/main/Maskify/model/deploy.prototxt)

   b. [res10_300x300_ssd_iter_140000.caffemodel](https://github.com/kr1shnasomani/Facetronix/blob/main/Maskify/model/res10_300x300_ssd_iter_140000.caffemodel)

   c. [model.h5](https://github.com/kr1shnasomani/Facetronix/blob/main/Maskify/model/model.h5)

4. Upon running the code, it will display the results in the specified path.

## Result:

  Input Image:

  ![image](https://github.com/user-attachments/assets/a18bbc51-fd04-4a53-ba6e-0105a4278928)

  Output Image:

  ![output](https://github.com/user-attachments/assets/ae105c89-404f-404a-9367-1116bb3f77d9)
