import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')
M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 180, 1)
img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('rotated cat', img_rotate)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()