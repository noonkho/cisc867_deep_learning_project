import os
import pandas as pd
import numpy as np
from PIL import Image
from tqdm import tqdm

def rle_decode(mask_rle, shape):
    '''
    Convert a RLE string to binary mask.
    '''
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape)

def rle_encode(img):
    '''
    Convert a binary mask to RLE.
    '''
    pixels = img.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)

def find_image_file(start_path, image_id):
    for file in os.listdir(start_path):
        if file.startswith(image_id) and file.endswith('.png'):
            return os.path.join(start_path, file)
    return None

def get_masks(csv_file, output_folder, target_size=(234, 234)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(csv_file)
    df['segmentation'] = df.segmentation.fillna('')

    # i = 0

    for _, row in tqdm(df.iterrows(), total=df.index.size, desc="Processing Mask"):

        # print(row['id'])
        # print(row['class'])
        # print(row['segmentation'])
        # print()
        # print(type(row['segmentation']))
        # if row['segmentation'] == "":
        #     print('yes')

        # i += 1
        # if i == 3:
        #     break
     
        if row['segmentation']:
            # print(row['segmentation'])
            # break
            img_arr = rle_decode(row['segmentation'], target_size)
            # print(img_arr)
            # Convert the np array to an image
            image = Image.fromarray(np.uint8(img_arr))

            # Save the true mask
            image_output_path = os.path.join(output_folder, f"{row['id']}_{row['class']}.png")
            image.save(image_output_path)


root_dir = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/'

csv_file = root_dir + 'cropped_database.csv'

output_folder = root_dir + 'true_masks'

get_masks(csv_file, output_folder)
