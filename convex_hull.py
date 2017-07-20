import argparse
import cv2
import imutils
import numpy as np

#load the image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to input image")
args = vars(ap.parse_args())

#prepare the image for contouring
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#imageCanny = cv2.Canny(blurred, 100, 200, 3)

#using hierarchy here
#RETR_EXTERNAL gives the contour of the external parent
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,255), 2)

cv2.imshow("Hull", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
