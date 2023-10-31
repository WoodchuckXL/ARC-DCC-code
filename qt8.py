#Identify balloon color

from djitellopy import Tello
from balloonIdentifier import BalloonIdentifier
import cv2

tello = Tello()
balloon = BalloonIdentifier()

tello.connect(True)

tello.streamon()

tello.takeoff()

while True:
    frame = tello.get_frame_read().frame
    if frame is not None:
        balloonData = balloon.identifyBalloon(frame)
        if balloonData is not None:
            corners, ids, rejected, colors = balloonData
            for i in range(len(ids)):
                print("The balloon with marker", ids[i], "is", colors[i])
            break
    if (cv2.waitKey(1) == 27): break
tello.land()