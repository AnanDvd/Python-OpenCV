import cv2
import numpy as np

img = cv2.imread('Lenna_gray.png',0)
rows, cols = img.shape #img.shape return a tuple which has the number of rows and columns


M = np.float32([[1,0,200], [0,1,67]]) #translating the matrix (image) by 200 px columns and 67 px rows
dst = cv2.warpAffine(img, M, (cols, rows)) #third argument is the size of the translated output image

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
