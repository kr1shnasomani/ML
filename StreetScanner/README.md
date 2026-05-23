<h1 align="center">StreetScanner</h1>

Semantic segmentation of pedestrians and vehicles in street view imagery.

## Approach
- **Deep Learning**: DeepLabv3 ResNet-50 model via PyTorch.
- **Segmentation**: Pixel-level masking and color-coded visualization.

## Performance
Accurate isolation of relevant traffic actors.

## Installation & Execution
```bash
cd StreetScanner
pip install -r requirements.txt
```
Run `code/both.py`, `code/pedestrian.py`, or `code/vehicle.py` depending on the desired target.
