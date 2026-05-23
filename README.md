<h1 align="center">Machine Learning Portfolio</h1>

A consolidated monorepo containing various projects across **Machine Learning**, **Deep Learning**, **Computer Vision**, and **Natural Language Processing**. 

This repository represents a structured collection of models ranging from classic OpenCV Haar cascades to modern Deep Learning architectures (ResNet50, YOLOv8, EfficientNetB3, DeepLabv3).

---

## 📂 Project Directory

### 👁️ Computer Vision
Traditional and deep learning-based image/video processing techniques.
* **[FaceCapture](./FaceCapture):** Detects and crops faces from static images using Haar cascade classifiers.
* **[FaceMeter](./FaceMeter):** Real-time facial landmark detection and visibility tracking using MediaPipe.
* **[OrthoVision](./OrthoVision):** Bone fracture detection from X-ray images using EfficientNetB3 via transfer learning.
* **[FireFinder](./FireFinder):** Fire detection from images using transfer learning with ResNet50.

### 🧠 Deep Learning, NLP & Predictive Modeling
Audio processing, sequence models, text processing, and tabular data analysis.
* **[CreditWise](./CreditWise):** Predicting credit card default probabilities using classification algorithms (XGBoost, LightGBM, Random Forest).
* **[ToneSense](./ToneSense):** Audio feature extraction (MFCCs) and emotion classification using a TensorFlow deep learning model.
* **[SentimentScope](./SentimentScope):** Text classification of IMDb movie reviews using LSTM networks and GloVe embeddings.
* **[FilmFinder](./FilmFinder):** Content-based movie recommendation engine utilizing NLP feature extraction (`CountVectorizer`, `TfidfVectorizer`) and cosine similarity.

### 🤖 Hybrid (CV + DL/NLP)
Multimodal projects combining visual and textual features.
* **[CaptionCraft](./CaptionCraft):** Image captioning generation combining DenseNet201 (visual features) and LSTM (text sequence generation).
* **[FaceFeel](./FaceFeel):** Facial emotion recognition utilizing a custom Convolutional Neural Network (CNN).
* **[Maskify](./Maskify):** Face mask detection using a Caffe model pipeline and a Keras binary classifier.
* **[PlateScan](./PlateScan):** Vehicle number plate contour isolation via OpenCV and optical character recognition (OCR) via EasyOCR.
* **[SpeedVision](./SpeedVision):** Real-time vehicle detection, tracking, and speed estimation using YOLOv8 and ByteTrack.
* **[StreetScanner](./StreetScanner):** Semantic pixel-level segmentation of pedestrians and vehicles using DeepLabv3 ResNet-50.
* **[WasteWise](./WasteWise):** Waste classification utilizing deep CNNs and extensive data augmentation, capable of exporting to TensorFlow Lite.

---

## 🚀 Getting Started

Each project is contained within its own folder and has its own `requirements.txt` or specific installation instructions. 

To run any individual project:
1. Clone the repository:
   ```bash
   git clone https://github.com/kr1shnasomani/ML.git
   cd ML
   ```
2. Navigate to the project directory:
   ```bash
   cd <ProjectName>
   ```
3. Install the specific dependencies (refer to the individual project's `README.md`):
   ```bash
   pip install -r requirements.txt
   ```
4. Execute the Python script or run the Jupyter Notebook.

---

## 🛠️ Global `.gitignore`

This repository uses a root `.gitignore` configured to keep out OS-specific metadata (`.DS_Store`), Python cache files (`__pycache__`), virtual environments, and Jupyter Notebook checkpoints. 

*Note: Some dataset files (like CSVs or heavy image/video folders) may require Git LFS if modified.*
