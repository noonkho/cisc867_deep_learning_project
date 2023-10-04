import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


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


def overlay_segmentation(image, mask, alpha=0.5, color='Reds'):
    """
    Overlay segmentation mask on the image.
    
    Parameters:
        image (np.array): Original image.
        mask (np.array): Binary segmentation mask.
        alpha (float): Opacity of the mask overlay, between 0 and 1.
        
    Returns:
        np.array: Visualized image with segmentation overlay.
    """
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.imshow(mask, cmap=color, alpha=alpha*(mask>0))
    plt.title("16-bit Grayscale Image")
    plt.axis('off')
    plt.show()


# image_path = "images/image1.png"
image_path = "/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/train/case123/case123_day0/scans/slice_0071_266_266_1.50_1.50.png"

img = mpimg.imread(image_path)

# Show image
plt.imshow(img, cmap="gray")
plt.title("16-bit Grayscale Image")

rle_string = "15314 2 15575 11 15840 13 16104 17 16369 19 16633 22 16897 25 17162 27 17428 27 17693 29 17959 29 18225 29 18490 31 18756 31 19021 32 19287 32 19552 33 19818 33 20083 34 20349 34 20615 34 20881 34 21147 33 21412 34 21678 33 21944 32 22210 29 22476 27 22742 24 23008 22 23274 18 23540 16 23807 14 24073 11 24341 6"
mask = rle_to_mask(rle_string, img.shape)
img_overlay = overlay_segmentation(img, mask)


