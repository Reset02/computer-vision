# Before trying to construct hybrid images, it is suggested that you
# implement my_imfilter.py and then debug it using hw1_test_filtering.py
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from my_imfilter import my_imfilter
from visualize_hybrid_image import visualize_hybrid_image
from normalize import normalize
from gauss2D import gauss2D

def main():
    """ function to create hybrid images """
    # read images and convert to floating point format

    main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # main_path = r"c://Users//lulu3//Desktop//HW1" # # 如果上述路徑不行，助教需使用這行程式，並且更改為自己的檔案路徑 r"路徑"

    # 不同圖片的合成
    # 2.1 
    image1 = cv2.cvtColor(cv2.imread(os.path.join(main_path, 'data', 'dog.bmp')), cv2.COLOR_BGR2RGB)
    image2 = cv2.cvtColor(cv2.imread(os.path.join(main_path, 'data', 'cat.bmp')), cv2.COLOR_BGR2RGB)
    # 2.2
    # image1 = cv2.cvtColor(cv2.imread(os.path.join(main_path, 'data', 'marilyn.bmp')), cv2.COLOR_BGR2RGB)
    # image2 = cv2.cvtColor(cv2.imread(os.path.join(main_path, 'data', 'einstein.bmp')), cv2.COLOR_BGR2RGB)
    # 2.3
    # image1 = cv2.cvtColor(cv2.imread(os.path.join(main_path, 'data', 'Putin.bmp')), cv2.COLOR_BGR2RGB)
    # image2 = cv2.cvtColor(cv2.imread(os.path.join(main_path, 'data', 'Trump.bmp')), cv2.COLOR_BGR2RGB)

    image1 = image1.astype(np.float32)/255
    image2 = image2.astype(np.float32)/255

    # Several additional test cases are provided for you, but feel free to make
    # your own (you'll need to align the images in a photo editor such as
    # Photoshop). The hybrid images will differ depending on which image you
    # assign as image1 (which will provide the low frequencies) and which image
    # you asign as image2 (which will provide the high frequencies)

    # ===============================================
    # === Filtering and Hybrid Image construction ===
    # ===============================================
    cutoff_frequency = 7 # This is the standard deviation, in pixels, of the 
    # Gaussian blur that will remove the high frequencies from one image and 
    # remove the low frequencies from another image (by subtracting a blurred
    # version from the original version). You will want to tune this for every
    # image pair to get the best results.
    gaussian_filter = gauss2D(shape=(cutoff_frequency*4+1,cutoff_frequency*4+1), sigma = cutoff_frequency)


    # =======================================================================
    # TODO: Use my_imfilter create 'low_frequencies' and                    
    # 'high_frequencies' and then combine them to create 'hybrid_image'     
    # =======================================================================
    # =======================================================================
    # Remove the high frequencies from image1 by blurring it. The amount of 
    # blur that works best will vary with different image pairs             
    # =======================================================================
    # 生成低頻成分
    low_frequencies = my_imfilter(image1, gaussian_filter)        # You need to modify here


    # ==========================================================================
    # Remove the low frequencies from image2. The easiest way to do this is to 
    # subtract a blurred version of image2 from the original version of image2.
    # This will give you an image centered at zero with negative values.       
    # ==========================================================================
    # 生成高頻成分
    # 高頻成分是從image2中去除低頻成分后的結果
    high_frequencies = image2 - my_imfilter(image2, gaussian_filter)       # You need to modify here


    # ==========================================================================
    # Combine the high frequencies and low frequencies                         
    # ==========================================================================
    # 生成混合圖像
    hybrid_image = normalize(low_frequencies + high_frequencies + 0.5)           # You need to modify here



    ### Visualize and save outputs ###
    plt.figure("Low Frequencies")
    plt.imshow(low_frequencies)
    plt.figure("High Frequencies")
    plt.imshow(normalize(high_frequencies + 0.5))
    hybrid_image_scales = visualize_hybrid_image(hybrid_image)
    plt.figure("Hybrid Image")
    plt.imshow(hybrid_image_scales)
    plt.imsave(os.path.join(main_path, 'results', 'low_frequencies.png'), low_frequencies, dpi=95)
    plt.imsave(os.path.join(main_path, 'results', 'high_frequencies.png'), normalize(high_frequencies + 0.5), dpi=95)
    plt.imsave(os.path.join(main_path, 'results', 'hybrid_image.png'), hybrid_image, dpi=95)
    plt.imsave(os.path.join(main_path, 'results', 'hybrid_image_scales.png'), hybrid_image_scales, dpi=95)

    plt.show()

if __name__ == '__main__':
    main()