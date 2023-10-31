import cv2
from cv2 import aruco

class ArucoReader:
    #Sets up an aruco reader object
    def __init__(self) -> None:
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
        self.parameters = cv2.aruco.DetectorParameters()

        # Change detector parameters here
        self.parameters.minCornerDistanceRate = 0.1

        self.detector = cv2.aruco.ArucoDetector(self.dictionary, self.parameters)

    #Searches an image for arUco tags and returns their IDs
    def checkForArUco(self, img: cv2.typing.MatLike):
        if img is None: return None
        markerData = self.detector.detectMarkers(img)
        corners, ids, rejected = markerData
        if ids is None: return None
        for i in ids: 
            #print(i, i[0])
            if (i[0] < 0 | i[0] > 999): return None

        """
        cv2.imwrite("balloonImage.png", cv2.aruco.drawDetectedMarkers(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), corners, ids))
        print(ids)
        #"""
        #Corners is an array of arrays in ascending order by the id of the tag. It goes in this order: top left, top right, bottom right, bottom left.
        #Ids is and array of the ids of the tags found sorted in ascending order
        return markerData
