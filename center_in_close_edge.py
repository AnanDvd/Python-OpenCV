'''
Encloses the outer edge.
Will try to use linearPolar() by detecting the center
'''

import argparse
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to input image")
args = vars(ap.parse_args())

def contoursConvexHull(contours):
    pts = []
    for i in range(0, len(contours)):
        for j in range(0, len(contours[i])):
            pts.append(contours[i][j])

    pts = np.array(pts)
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

    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

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

plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
