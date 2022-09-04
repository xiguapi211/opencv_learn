# author: ray
# date: 2022/9/4
import cv2
import numpy as np

#
cv2.namedWindow('win', cv2.WINDOW_NORMAL)
img = cv2.imread('./small.png', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
# 一个随机数 shape
key = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)
encryption = cv2.bitwise_xor(img, key)

cv2.imshow('win', img)
cv2.waitKey(0)

cv2.imshow('win', encryption)
cv2.waitKey(0)
cv2.destroyAllWindows()

