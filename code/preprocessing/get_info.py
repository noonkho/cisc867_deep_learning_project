import os
from PIL import Image
import numpy as np

def get_png_files(root_dir):
    """
    Traverse the directory structure and find all PNG files.
    """
    png_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".png"):
                png_files.append(os.path.join(root, file))
    return png_files

def get_image_shape(image_path):
    """
    Get the shape of the image.
    """
    with Image.open(image_path) as img:
        return np.array(img).shape

def find_unique_shapes(root_dir):
    """
    Find all unique shapes of PNG images in the given directory structure.
    """
    png_files = get_png_files(root_dir)
    unique_shapes = set()

    for file in png_files:
        shape = get_image_shape(file)
        unique_shapes.add(shape)

    return unique_shapes

# Find all the shapes of the images
root_dir = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/train'  # Replace with the path to your 'train' directory
unique_shapes = find_unique_shapes(root_dir)
print("Unique shapes found:", unique_shapes)
