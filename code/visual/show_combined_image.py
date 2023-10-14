import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import os

def rle_to_mask(mask_rle, shape):
    '''
    Convert RLE encoding to binary mask. Reference: https://ccshenyltw.medium.com/run-length-encode-and-decode-a33383142e6b

    Parameters:
        mask_rle: run-length as string formatted (start length)
        shape: (height, width) of the array to return 
    
    Returns:
        numpy array, 1 - mask, 0 - background
    '''
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0] * shape[1], dtype=np.uint16)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape)

def stack_segmentations(image, masks, legend, title="16-bit Grayscale Image", alpha=0.5, colors=['Reds', 'Greens', 'Blues']):
    """
    Display the given image with segmentation masks overlay on the image.
    
    Parameters:
        image (np.array): Original image
        masks ([Str]): list of RLE, should be length of 3
        legend ([Str]): legend for each mask, should be length of 3

    Optional Parameters:
        title (Str): title of the image
        alpha (float): Opacity of the mask overlay, between 0 and 1
        color ([Str])
        title (Str)
        
    Returns:
        Null
    """
    segments = []

    plt.figure()
    plt.imshow(image, cmap='gray')

    for idx, rle in enumerate(masks):
        if rle != "nan":
            mask = rle_to_mask(rle, image.shape)
            print("mask",idx,"done")
            temp = plt.imshow(mask, cmap=colors[idx], alpha=alpha*(mask>0))
            segments.append(mpatches.Patch(color=plt.get_cmap(colors[idx])(0.5), alpha=1, label=legend[idx]))
            
    plt.title(title)
    plt.axis('off')
    plt.legend(handles=segments, loc=1, bbox_to_anchor=(1.2, 1)) # bbox_to_anchor shift the legend (x,y)
    plt.show()


def get_path(root_dir, id, full_path_bool=False):
    """
    Return the path of the MRI image based on id

    Parameters:
        root_dir (String): the root directory ends with /
        id (String): id
        full_path_bool (Boolean): a boolean to indicate return full path or relative path
    
    Returns:
        String: a full/relative path of the image of that id
    """
    lis = id.split("_") # [0] = case no. [1] = day no. [2] = slice [3] slice no.

    path = root_dir + "train/" + lis[0] + "/" + lis[0] + "_" + lis[1] + "/scans/"

    for folder, subfolders, files in os.walk(path):
        if folder != root_dir:
            for f in files:
                if f.startswith("slice_" + lis[3]):
                
                    full_path = os.path.join(folder, f)
                    if full_path_bool:
                        return full_path
                    else:
                        return full_path[full_path.startswith(root_dir) and len(root_dir):]
    return "ERROR: image file cannot be found"


# Load Dataset and Rootdir
root_dir = "/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/"
file_path = '/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/cisc867_deep_learning_project/data/combined_class.csv'

df = pd.read_csv(file_path, converters={"class": lambda x: x.replace("'","").strip("[]").split(", "), 
                                        "segmentation": lambda x: x.replace("'","").strip("[]").split(", ")})


# Show image using a row in the dataset
# row = df.loc[81] # random
# print(row)

# print(df.index[df["id"] == "case123_day0_slice_0071"]) # Select one with all 3 segments
row = df.loc[6806]
print(row)

image_path = get_path(root_dir, row["id"], True)

img = mpimg.imread(image_path)

# Show image
# plt.imshow(img, cmap="gray")
# plt.title("16-bit Grayscale Image")
# plt.show()


# Show image with all the labels
stack_segmentations(img, row["segmentation"], row["class"], "case123_day0_slice_0071") 
