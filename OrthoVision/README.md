<h1 align="center">OrthoVision</h1>

Deep learning Computer Vision model for Bone Fracture Detection from X-ray images.

## Approach
- **Transfer Learning**: EfficientNetB3 base feature extractor.
- **Optimization**: Uses `ModelCheckpoint`, `EarlyStopping`, and `ReduceLROnPlateau` callbacks.

## Performance
High precision fracture classification avoiding overfitting.

## Installation & Execution
```bash
cd OrthoVision
pip install numpy matplotlib opencv-python scikit-learn tensorflow
```
Open and run `code/main.ipynb`.
