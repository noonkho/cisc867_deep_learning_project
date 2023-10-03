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
    img = np.zeros(shape[0] * shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T  # Needed to align to RLE direction


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
image_path = "/Users/echingkho/Desktop/University/Master/1st_year/Fall/dl_cisc_867/project/uw-madison-gi-tract-image-segmentation/train/case123/case123_day20/scans/slice_0067_266_266_1.50_1.50.png"

img = mpimg.imread(image_path)

# Show image
plt.imshow(img, cmap="gray")
plt.title("16-bit Grayscale Image")

rle_string = "15323 4 15587 8 15852 10 16117 11 16383 12 16649 12 16915 12 17181 12 17447 12 17713 12 17979 12 18245 12 18511 12 18777 12 19043 12 19309 12 19575 12 19841 12 20107 12 20373 12 20639 12 20905 12 21171 12 21437 12 21703 12 21969 12 22235 12 22501 12 22767 12 23033 12 23299 12 23565 12 23831 12 24097 12 24363 12 24629 12 24895 12 25161 13 25427 13 25693 14 25959 14 26224 15 26489 16 26755 17 27020 19 27286 20 27552 21 27818 21 28084 21 28350 22 28616 22 28882 22 29147 23 29413 23 29678 24 29944 24 30210 25 30476 25 30742 25 31008 25 31274 25 31540 25 31806 25 32072 24 32338 24 32604 24 32871 22 33137 22 33403 21 33669 21 33936 19 34203 17 34469 14 34736 12 35003 11 35271 8 35539 3"
mask = rle_to_mask(rle_string, img.shape)
img_overlay = overlay_segmentation(img, mask)


