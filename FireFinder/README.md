<h1 align="center">FireFinder</h1>

Deep learning-based Fire Detection System built to identify fire outbreaks from images.

## Approach
- **Transfer Learning**: Pre-trained ResNet50 model as the base.
- **Custom Top Layers**: Global Average Pooling and Dropout for robust binary classification.
- **Data Augmentation**: `ImageDataGenerator`.

## Performance
High accuracy tracking through confusion matrix and classification reports.

## Installation & Execution
```bash
cd FireFinder
pip install numpy matplotlib opencv-python scikit-learn tensorflow
```
Open and run `code/main.ipynb`.
