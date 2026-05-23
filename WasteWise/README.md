<h1 align="center">WasteWise</h1>

Waste image classifier identifying and categorizing different types of waste.

## Approach
- **Architecture**: Deep Convolutional Neural Network built with Keras/TensorFlow.
- **Augmentation**: Extensively uses `ImageDataGenerator`.
- **Export**: Converts the finalized model into TensorFlow Lite (`.tflite`).

## Performance
Achieves >97% validation accuracy with early stopping mechanisms.

## Installation & Execution
```bash
cd WasteWise
pip install numpy matplotlib opencv-python scikit-learn tensorflow
```
Open and run `code/main.ipynb`.
