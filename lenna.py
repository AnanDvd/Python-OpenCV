import numpy as np
import cv2


img = cv2.imread('Lenna.png', 0) #loads image in greyscale
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): #return 115 (dec value of 's')
    cv2.imwrite('LenaOpenCV', img)
    cv2.destroyAllWindows()
    
    

