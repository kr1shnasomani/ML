<h1 align="center">CaptionCraft</h1>

Image captioning model generating descriptive captions for images from the Flickr8k dataset.

## Approach
- **Feature Extraction**: DenseNet201 for computer vision.
- **Sequence Prediction**: LSTM for NLP token generation.
- Built with TensorFlow/Keras.

## Performance
Trained on Flickr8k. Evaluated over multiple epochs, saving weights to `model.keras`.

## Installation & Execution
```bash
cd CaptionCraft
pip install -r requirements.txt
```
Open and run `code/main.ipynb` to train the model and generate captions.
