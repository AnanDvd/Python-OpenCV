import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

#drawing a line: pass the starting and ending coordinates
#diagonal blue line with thickness of 5 px
cv2.line(img, (0,0), (511,511), (255,0,0), 5)

#rectangle: top-left and bottom-right corner
#green rectangle at the top-right corner of the image
cv2.rectangle(img, (384,0), (510,128), (0,255,0),3)

#circle: coordinates of center, and radius
#drawing a circle inside the above rectangle
cv2.circle(img, (447,63), 63, (0,0,255), -1)

#ellipse: check cv2.ellipse() documentation
''' To draw the ellipse, we need to pass several arguments.
One argument is the center location (x,y). Next argument is
axes lengths (major axis length, minor axis length). angle is
the angle of rotation of ellipse in anti-clockwise direction.
startAngle and endAngle denotes the starting and ending of
ellipse arc measured in clockwise direction from major axis.
i.e. giving values 0 and 360 gives the full ellipse.
For more details, check the documentation of cv2.ellipse().
Below example draws a half ellipse at the center of the image.'''
cv2.ellipse(img, (256,256), (100,50), 0,0,180, 255, -1)

#polygon
'''To draw a polygon, first you need coordinates of vertices.
Make those points into an array of shape ROWSx1x2 where ROWS are
number of vertices and it should be of type int32. Here we draw
a small polygon of with four vertices in yellow color. ''' 
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts= pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255))

#adding text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (100,500), font, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('draw', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
