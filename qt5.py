# Team Selfie

from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()

tello.takeoff()

tello.move_up(50)

tello.streamon()

# Takes selfie
selfie = tello.get_frame_read().frame

tello.streamoff()

tello.land()

#Displays selfie
cv2.imshow(selfie)
cv2.waitKey()