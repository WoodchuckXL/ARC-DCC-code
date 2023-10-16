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
    def checkForArUco(self, img: cv2.typing.MatLike) -> int:
        if img is None: return None
        markerData = self.detector.detectMarkers(img)
        corners, ids, rejected = markerData
        if ids is None: return None
        for i in ids: 
            if (i < 0 | i > 999): return None
        cv2.imshow('tags detected', cv2.aruco.drawDetectedMarkers(img,corners, ids))
        cv2.waitKey()
        #Corners is an array of arrays in ascending order by the id of the tag. It goes in this order: top left, top right, bottom right, bottom left.
        #Ids is and array of the ids of the tags found sorted in ascending order
        return markerData
