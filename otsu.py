import cv2
import numpy as np

import timeit

import cv2
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

def otsu_threshold(img):
    #blur = cv2.GaussianBlur(img, (9, 9), 0)
    _, thresholded = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img, thresholded

def process_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    print(image_path)
    original_img, thresholded_img = otsu_threshold(img)
    return original_img, thresholded_img

  
def otsu(image_paths):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_image, image_paths))

    for original_img, thresholded_img in results:
        plt.subplot(1, 2, 1), plt.imshow(original_img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])

        plt.subplot(1, 2, 2), plt.imshow(thresholded_img, cmap='gray')
        plt.title("Otsu's Thresholding"), plt.xticks([]), plt.yticks([])

        plt.show()
  
if __name__ == "__main__":
    image_paths = ["0.bmp", "2.bmp", "701.bmp"]

    elapsed_time_paralell = timeit.timeit(lambda: otsu(image_paths), number=1)
    print('elapsed_time_paralell: ', elapsed_time_paralell)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
