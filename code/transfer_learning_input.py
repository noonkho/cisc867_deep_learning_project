"""
Show scan files.
"""
from PIL import Image

img = Image.open(r"../data/train/case2/case2_day1/scans/slice_0001_266_266_1.50_1.50.png")
img.show("Scan")