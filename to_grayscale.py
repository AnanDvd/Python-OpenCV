import cv2

image = cv2.imread('Lenna.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Lenna_gray.png', gray_image)
cv2.imshow('Lenna.png', image)
cv2.imshow('Lenna_gray', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
