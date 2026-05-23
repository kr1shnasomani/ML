<h1 align="center">SpeedVision</h1>

Real-time vehicle detection, tracking, and speed estimation.

## Approach
- **Detection**: YOLOv8 state-of-the-art object detection.
- **Tracking**: ByteTrack for object continuity across frames.
- **Calculations**: OpenCV for distance-over-time speed calculations.

## Performance
Real-time processing and annotation of video files.

## Installation & Execution
```bash
cd SpeedVision
pip install -r requirements.txt
python code/main.py
```
