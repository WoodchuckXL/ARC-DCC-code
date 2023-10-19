from djitellopy import Tello
import cv2
from cv2 import aruco
import time
from arucoReader import ArucoReader
from identifyColor import ColorIdentifier

class BalloonIdentifier:
    def __init__(self) -> None:
        self.tagReader = ArucoReader()
        self.colorReader = ColorIdentifier()    

    def _getTagColors(self, img, markerData) -> str:
        corners, ids, rejected = markerData
        
        for i in range(len(ids)):
            print("The balloon with marker", i, "is", self.getColor(img, corners[i][0]))
        return None

    def _getColor(self, img, corners) -> str:

        length = corners[1][0] - corners[0][0]
        height = corners[3][1] - corners[0][1]

        #print(length, height)
        
        percent = 0.025

        horOffset = [-1, 1, 1, -1]
        verOffset = [-1, -1, 1, 1]

        cornerColors = [''] * 4
        for i in range(4):

            x = int(corners[i][0] + (horOffset[i] * percent) * length)
            y = int(corners[i][1] + (verOffset[i] * percent) * height)

            pixel = img[y, x]
            cornerColors[i] = self.colorReader.getColorStr(pixel)

        # Create a dictionary to store the count of each color
        colorDict = {}

        # Iterate through the array
        for color in cornerColors:
            if color in colorDict:
                colorDict[color] += 1
            else:
                colorDict[color] = 1

        # Check for colors with a count of 3 or more
        for color, count in colorDict.items():
            if count >= 3:
                return color
        return None

    def identifyBalloon(self, img):
        markerData = self.tagReader.checkForArUco(img)
        if markerData is not None:
            self._getTagColors(img, markerData)

    

def main():

    tello = Tello()

    tello.connect(True)

    battery = tello.get_battery()
    print("Battery life is " + str(tello.get_battery()) + "%.")
    if (battery <= 10):
        print("Aborting...")
        return

    
    tello.streamon()
    balloon = BalloonIdentifier()

    while True:
        frame = tello.get_frame_read().frame
        
        #balloon.identifyBalloon(frame)

        cv2.imshow('tello_cam', frame)
        if (cv2.waitKey(1) == 27): break
    

if __name__ == "__main__":main()