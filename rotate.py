import cv2

img = cv2.imread('Lenna_gray.png', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90,1) #rotating about the center by 90 deg
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroAllWindows()
