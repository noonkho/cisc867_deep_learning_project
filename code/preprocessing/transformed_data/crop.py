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

def crop_center(img, cropx, cropy):
    y, x = img.shape[0], img.shape[1]
    startx = x//2-(cropx//2)
    starty = y//2-(cropy//2)    
    return img[starty:starty+cropy, startx:startx+cropx]

def find_image_file(start_path, image_id):
    for file in os.listdir(start_path):
        if file.startswith(image_id) and file.endswith('.png'):
            return os.path.join(start_path, file)
    return None

def process_images_and_masks(csv_file, images_folder, output_folder, output_csv, target_size=(234, 234)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(csv_file)
    grouped = df.groupby('id')
    new_rows = []
    # testing = False

    for image_id, group in tqdm(grouped, desc="Processing images"):
        image_path = find_image_file(images_folder, image_id)

        # print(image_id)
        # print(group)
        # break
        
        if image_path:
            with Image.open(image_path) as img:
                img_cropped = crop_center(np.array(img), *target_size)
                # Image.fromarray(img_cropped).save(os.path.join(output_folder, f"{image_id}.png"))
            
            for _, row in group.iterrows():
                class_label, segmentation = row['class'], row['segmentation']
        #         if not pd.isna(segmentation):
        #             print(segmentation)
        #             print(type(segmentation))
        #             testing=True
        #             break
        # if testing:
        #     break

                if pd.notna(segmentation):
                    mask = rle_decode(segmentation, img.size)
                    mask_cropped = crop_center(mask, *target_size)
                    new_rle = rle_encode(mask_cropped)
                    new_rows.append({'id': image_id, 'class': class_label, 'segmentation': new_rle})
                else:
                    new_rows.append({'id': image_id, 'class': class_label, 'segmentation': np.nan})

    new_df = pd.DataFrame(new_rows)
    new_df.to_csv(output_csv, index=False)


csv_file = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/train.csv'
images_folder = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/dataset'
output_folder = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/cropped_database'
output_csv = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/cropped_database.csv'
process_images_and_masks(csv_file, images_folder, output_folder, output_csv)
