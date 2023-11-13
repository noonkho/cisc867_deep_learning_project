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
image_path = "/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/cropped_database/case101_day20_slice_0067.png"

img = mpimg.imread(image_path)

# Show image
plt.imshow(img, cmap="gray")
plt.title("16-bit Grayscale Image")
# plt.show()

rle_string = "23809 2 24041 7 24273 10 24505 14 24737 17 24969 20 25202 23 25436 24 25669 26 25903 26 26137 27 26371 27 26605 27 26839 27 27074 26 27308 26 27543 25 27777 25 28012 24 28246 23 28481 22 28715 21 28949 21 29184 19 29418 19 29652 18 29887 16 30122 14 30357 12 30592 10 30829 4"
mask = rle_to_mask(rle_string, img.shape)
img_overlay = overlay_segmentation(img, mask)


