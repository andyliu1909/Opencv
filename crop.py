import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./lenna.jpg', 1)
"""
cv2.imshow('lenna', img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()
plt.imshow(img)
plt.show()

B, G, R = cv2.split(img)
img_rgb = cv2.merge((R, G, B))
plt.imshow(img_rgb)
plt.show()
"""

img_crop = img[200:400, 200:400]
cv2.imshow('img_crop', img_crop)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()