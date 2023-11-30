from balloon import Balloon
import cv2
import numpy as np
import cameraMatrices
import math

class BalloonTracker:
    balloons = []
    droneSerialNumber = "F5"
    markerSize = 5
    markerPoints = None
    def __init__(self, serialNumber : str, arucoMarkerSize : float) -> None:
        self.droneSerialNumber = serialNumber
        self.markerSize = arucoMarkerSize
        self.markerPoints = np.array([[-self.markerSize / 2, self.markerSize / 2, 0],
                                      [self.markerSize / 2,  self.markerSize / 2, 0],
                                      [self.markerSize / 2, -self.markerSize / 2, 0],
                                      [-self.markerSize / 2,-self.markerSize / 2, 0]], dtype=np.float32)
        return None
    
    def updateBalloonList(self, imageBalloonData, dx : float, dy : float, yaw : int):
        if imageBalloonData is None: return

        corners, ids, rejected, colors = imageBalloonData

        for i in range(len(corners)):
            if colors[i] is not None and colors[i] is not "gray" and colors[i] is not "white" and colors[i] is not "black": 
                balloonExists = False
                for balloon in self.balloons:
                    if balloon is not None and balloon.equals(ids[i], colors[i]):
                        balloon.addPosition(self._getBalloonPos(dx, dy, yaw, corners[i]))
                        balloonExists = True
                if not balloonExists:
                    ball = Balloon(ids[i], colors[i])
                    ball.addPosition(self._getBalloonPos(dx, dy, yaw, corners[i]))
                    self.balloons.append(ball)
        

    def _getBalloonPos(self, dx : float, dy : float, yaw : int, corners) -> tuple([float, float]):
        trash, rvec, tvec = cv2.solvePnP(self.markerPoints, corners, cameraMatrices.cameraMatrices[self.droneSerialNumber], cameraMatrices.distCoeffs[self.droneSerialNumber], False, cv2.SOLVEPNP_IPPE_SQUARE)
        
        relativeAngle = math.atan2(tvec[0][0], tvec[2][0])
        worldAngle = (yaw + 180 + math.degrees(relativeAngle))%360 - 180

        hypotenuse = (tvec[0][0]**2 + tvec[2][0]**2)**0.5

        relX = math.sin(math.radians(worldAngle)) * hypotenuse
        relY = math.cos(math.radians(worldAngle)) * hypotenuse

        worldX = dx + relX
        worldY = dy + relY

        print("world:", worldX, worldY, "rel:", relX, relY)

        return tuple([worldX, worldY])
    
    def removeRepeats(self):
        removeAbles = []

        for balloon in self.balloons:
            aId = balloon.tagId
            aPos = balloon.getPosition()
            for b in self.balloons:
                print(balloon.color, balloon.tagId, balloon.count)
                print(b.color, b.tagId, b.count)
                bPos = b.getPosition()
                if b.tagId == aId:
                    if ((aPos[0] - bPos[0])**2 + (aPos[1] - bPos[1])**2)**0.5 < 1:
                        #Both balloons are in the same position with the same Id and different colors
                        if balloon.count > b.count:
                            removeAbles.append(b)

        for ballRem in removeAbles:
            self.balloons.remove(ballRem)

    def removeFalsePositives(self):
        removeAbles = []

        for balloon in self.balloons:
            if balloon.tagId == 0 or balloon.tagId > 999:
                removeAbles.append(balloon)

        for ballRem in removeAbles:
            self.balloons.remove(ballRem)

    def printBalloonList(self):
        self.removeFalsePositives()
        self.removeRepeats()
        print("Balloons Found:")
        for balloon in self.balloons:
            pos = balloon.getPosition()
            print(balloon.color, balloon.tagId, "Pos(cm):", pos, "Pos(ft):", 0.0328084*pos[0], 0.0328084*pos[1])