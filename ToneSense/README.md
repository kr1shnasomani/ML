<h1 align="center">ToneSense</h1>

Classifies human emotions (happiness, sadness, anger) from audio files.

## Approach
- **Feature Extraction**: MFCCs and spectral features via Librosa.
- **Deep Learning**: TensorFlow neural network processing audio spectrogram features.

## Performance
Outputs a trained `model.keras` evaluated over multiple epochs.

## Installation & Execution
```bash
cd ToneSense
pip install -r requirements.txt
```
Open and run `code/main.ipynb`.
