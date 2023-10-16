import numpy as np
import arucoReader as ar
import identifyColor as ic
import cv2



#""" #ArUco identification Testing
ar.initArUcoReader()

img = cv2.imread('/Users/james/Documents/School/ARC/Tello3.9/src/balloon_mockup.png', cv2.IMREAD_COLOR)
markerData = ar.checkForArUco(img)
corner, ids, rejected = markerData
#print(corner)

getTagColors(img, markerData)
#"""

""" #Color identification and masking
img = cv2.imread('/Users/james/Documents/School/ARC/Tello3.9/src/pridecurve.png', cv2.IMREAD_COLOR)
ic.createColorMask(img,'red')
print(ic.getColorStr(img[0,0]))
#"""

