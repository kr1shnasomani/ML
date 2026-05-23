<h1 align="center">Maskify</h1>

Detects faces and predicts whether the person is wearing a mask.

## Approach
- **Face Detection**: Caffe model for robust bounding box detection.
- **Classification**: Keras-based deep learning classifier for Mask/No Mask labeling.

## Performance
High accuracy on standard static images.

## Installation & Execution
```bash
cd Maskify
pip install -r requirements.txt
python code/main.py
```
