import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
edges = cv2.Canny(image, 100, 200)

plt.subplot(121)
plt.imshow(image, cmap = 'gray')
plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image')
plt.xticks([]), plt.yticks([])

plt.show()
