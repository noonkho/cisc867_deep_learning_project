import os
from PIL import Image
from tqdm import tqdm

def get_png_files(directory):
    """
    List all PNG files in the specified directory.
    """
    return [f for f in os.listdir(directory) if f.endswith('.png')]

def get_image_shape(image_path):
    """
    Get the shape of the image.
    """
    with Image.open(image_path) as img:
        return img.size  # Returns a tuple (width, height)

def find_unique_shapes(directory):
    """
    Find all unique shapes of PNG images in the given directory.
    """
    png_files = get_png_files(directory)
    unique_shapes = set()

    for filename in tqdm(png_files, total=len(png_files), desc="Counting image"):
        file_path = os.path.join(directory, filename)
        shape = get_image_shape(file_path)
        unique_shapes.add(shape)

    return unique_shapes

# directory = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/dataset'
directory = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/cropped_database'
unique_shapes = find_unique_shapes(directory)
print("Unique shapes found:", unique_shapes)
