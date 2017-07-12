import cv2
import argparse
import imutils
import numpy as np

'''ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

img = cv2.imread(args["cilia.jpg"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('new', img)
cv2.waitKey(0)
cv2.destroAllWindows()'''

circleArr = np.ndarray((512,512), dtype=np.float32)
for i in range(10,600,10):
    cv2.circle(circleArr, (256,256), i-10, np.random.randint(60,500), thickness = 4)

lp = np.ndarray((512,512), dtype=np.float32)
img1 = cv2.linearPolar(circleArr, (256,256), 100, cv2.INTER_LINEAR+cv2.WARP_FILL_OUTLIERS)

'''from scipy.misc import toimage
toimage(lp, mode="L").show()'''

cv2.imshow('array', circleArr)
cv2.imshow("polar image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
    



