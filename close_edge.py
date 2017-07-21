'''
Encloses the individual microtubules
We will try to use the individual microtubules for
flattening if linearPolar() fails
'''

import argparse
import cv2
import imutils
import numpy as np


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


image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
imageCanny = cv2.Canny(blurred, 100, 200, 3)

img, contours, hierarchy = cv2.findContours(imageCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,255), 2)


ConvexHullPoints = contoursConvexHull(contours)
cv2.polylines(image, [ConvexHullPoints], True, (0,255,255), 2)


cv2.imshow("Hull", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
hull = cv2.convexHull(cnts)

for c in hull:
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0,0

        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
'''

