import cv2
import numpy as np

img = cv2.imread('Lenna.png')

px = img[100,100]
print (px) #prints the [b,g,r] values of the pixel. For a grayscle image, it just returns the internsity

#accessing only the blue pixel
blue = img[100,100,0]
print (blue)


#modifying the pixel values
img[100,100] = [255,255,255]
print (img[100,100])

print (img.shape) #prints the tuple of rows, columns and channels (for color image)
                  #for grayscale, return only the number of rows and columns


    
print (img.size) #total number of pixels in the image

print (img.dtype) #image datatype


#make all the red pixels zero
img[:,:,2] = 0 

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
