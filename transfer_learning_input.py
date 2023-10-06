"""
Finding input formats for the various pre-trained models we hope to use for
transfer learning.

Potential models:
- Model (Size, params, depth)

- VGG16 (528 MB, 138.4M, 16)
- ResNet50V2 (98 MB, 25.6M, 103)
- InceptionV3 (92 MB, 23.9M, 189)
- EfficientNetB4 (75MB, 19.5M, 258)

Look into 'Build InceptionV3 over a custom input tensor'
"""

from PIL import Image

img = Image.open(r"C:/Users\tdsel/Documents/courses/cisc867/cisc867_deep_learning_project/data/train/case2/case2_day1"
                 r"/scans/slice_0001_266_266_1.50_1.50.png")
img.show("Scan")