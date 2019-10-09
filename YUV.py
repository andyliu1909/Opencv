import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img_dark = cv2.imread('.\cat.jpg')
cv2.imshow('img_dark', img_dark)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype('uint8')
    return cv2.LUT(img_dark, table)


img_brighter = adjust_gamma(img_dark, 2)
cv2.imshow('img_dark', img_dark)
cv2.imshow('img_brighter', img_brighter)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()

img_small_brighter = cv2.resize(img_brighter, (int(img_brighter.shape[1] * 0.5), int(img_brighter.shape[0] * 0.5)))
plt.hist(img_brighter.flatten(), 256, [0, 256], color='r')
plt.show()

img_yuv = cv2.cvtColor(img_small_brighter, cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
cv2.imshow('color input image', img_small_brighter)
cv2.imshow('Histogram equalized', img_output)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()