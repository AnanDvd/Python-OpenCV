'''
Encloses the outer edge.
Will try to use linearPolar() by detecting the center
and maxRadius
'''

import argparse
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import math

#loading the image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to input image")
args = vars(ap.parse_args())


def contoursConvexHull(contours):
    pts = []
    for i in range(0, len(contours)):
        for j in range(0, len(contours[i])):
            pts.append(contours[i][j])

    pts = np.array(pts)
    #print (pts)
    result = cv2.convexHull(pts)
    return result

#Prepares the image for contouring
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
imageCanny = cv2.Canny(blurred, 100, 200, 3)

img, contours, hierarchy = cv2.findContours(imageCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image, contours, -1, (0,255,255), 2)


ConvexHullPoints = contoursConvexHull(contours)
cv2.polylines(image, [ConvexHullPoints], True, (0,255,255), 2)

#polylines() gives the required outer edge
#now we find the center of this contour (edge)
#which will serve as the center for linearPolar()

'''for c in cv2.polylines(image, [ConvexHullPoints], True, (0,255,255), 2):
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        #print (cX,cY)
    else:
        cX, cY = 0,0
        #print (cX,cY)
'''

'''cnt = contours[cv2.polylines(image, [ConvexHullPoints], True, (0,255,255), 2)]
M = cv2.moments(cnt)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print (cX,cY)
else:
    cX, cY = 0,0
    print (cX,cY)

    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
'''
#Takes the area as parameter to find center
c = max(contours, key = cv2.contourArea)
M = cv2.moments(c)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print (cX,cY)
else:
    cX, cY = 0,0
    print (cX,cY)

    #cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    #cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

'''
looks like we are getting the center of the external contour [232, 192]
but it doesn't display in the image, what the last two lines of code should do
we can try opening the image in matplotlib to approximate if the center is close
to [232, 192]
'''

'''
cv2.imshow("Hull", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
linearPolar(src, center, maxRadius, flags)
We already have the center (cX, cY). We need to find the maxRadius,
i.e. distance from the center to the farthest point on the contour
'''
#extremeX = tuple(c[c[:,:,0].argmax()][0])
#extremeY = tuple(c[c[:,:,1].argmax()][0])
#print (extremeX, extremeY)
#perimeter = cv2.arcLength(contours, True)
#print (perimeter)
#cv2.circle(image, extremeX, 8, (0, 255, 0), -1)
#cv2.circle(image, extremeY, 8, (255,255,0), -1)


'''
ConvexHullPoints is the array that stores the location of the values
of the exterior contour. We will loop over this array, and for every point,
calcualte the distance of that point from the center (cX, cY). ConvexHullPoint
has 35 points. 
'''
cpts = []
cpts.append(ConvexHullPoints)
cpts = np.array(cpts)
#print (cpts[0,int(cpts.size/2) - 1])
#print (cpts[0,1])
#print (cpts[0,int(cpts.size/2 - 1)][0][1])


#for i in range(0, int(cpts.size/2 - 1)):
 #   dist[] = 
    
    

polarImage = cv2.linearPolar(image, (cX,cY), 200, cv2.INTER_LINEAR+cv2.WARP_FILL_OUTLIERS)

'''
Rotating the image
rows, cols = polarImage.shape
R = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(polarImage, R, (cols, rows))
'''

plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.imshow(polarImage, cmap = 'gray', interpolation = 'bicubic')
cv2.imshow("Flatten", polarImage)
plt.xticks([]), plt.yticks([])
plt.show()
