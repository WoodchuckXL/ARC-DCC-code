from arucoReader import ArucoReader
import identifyColor as ic
import cv2

#""" #ArUco identification Testing
ar = ArucoReader()

img = cv2.imread('src/testimg/balloon_mockup.png', cv2.IMREAD_COLOR)
markerData = ar.checkForArUco(img)
corner, ids, rejected = markerData
#print(corner)

#"""

""" #Color identification and masking
img = cv2.imread('/Users/james/Documents/School/ARC/Tello3.9/src/pridecurve.png', cv2.IMREAD_COLOR)
ic.createColorMask(img,'red')
print(ic.getColorStr(img[0,0]))
#"""

