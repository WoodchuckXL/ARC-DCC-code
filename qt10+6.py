# Draw arUco Tag numbers

from djitellopy import Tello
from arucoReader import ArucoReader
import cv2

u = 20
speed = 20

def flyNumPattern(num : int, tello : Tello):
    if num == 0: 
        numPattern(0, tello)
        return
    
    digitCount = 0
    tempNum = num
    while tempNum != 0:
        tempNum //= 10
        digitCount += 1

    digits = [0] * digitCount
    tempNum = num
    for i in range(digitCount):
        digits[digitCount - 1 - i] = tempNum % 10
        tempNum //=10

    for digit in digits:
        numPattern(digit, tello)


def numPattern(digit: int, tello : Tello):
    if (digit == 1):
        tello.go_xyz_speed(1*u, 2*u, 0, speed)
        tello.go_xyz_speed(2*u, -2*u, 0, speed)
        tello.go_xyz_speed(-6*u, 0, 0, speed)
        tello.go_xyz_speed(0, 2*u, 0, speed)
        tello.go_xyz_speed(0, -4*u, 0, speed)
        tello.go_xyz_speed(3*u, 2*u, 0, speed)
    elif (digit == 2):
        tello.go_xyz_speed(1*u, 2*u, 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(-1*u, 3*u, 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(0, -4*u, 0, speed)
        tello.go_xyz_speed(3*u, 2*u, 0, speed)
    elif (digit == 3):
        tello.go_xyz_speed(1*u, 2*u, 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(-1*u, 1*u, 0, speed)
        tello.go_xyz_speed(0, 2*u, 0, speed)
        tello.go_xyz_speed(0, -2*u, 0, speed)
        tello.go_xyz_speed(-1*u, -1*u, 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(1*u, -2*u, 0, speed)
    elif (digit == 4):
        tello.go_xyz_speed(-3*u, -1*u, 0, speed)
        tello.go_xyz_speed(6*u, 0, 0, speed)
        tello.go_xyz_speed(-4*u, 3*u, 0, speed)
        tello.go_xyz_speed(0, -4*u, 0, speed)
        tello.go_xyz_speed(1*u, 2*u, 0, speed)
    elif (digit == 5):
        tello.go_xyz_speed(3*u, -2*u, 0, speed)
        tello.go_xyz_speed(0, 4*u, 0, speed)
        tello.go_xyz_speed(-3*u, 0, 0, speed)
        tello.go_xyz_speed(1*u, -2*u, 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(1*u, -2*u, 0, speed)
    elif (digit == 6):
        tello.go_xyz_speed(1*u, -2*u, 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(-2*u, 0, 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
    elif (digit == 7):
        tello.go_xyz_speed(3*u, 2*u, 0, speed)
        tello.go_xyz_speed(0, -4*u, 0, speed)
        tello.go_xyz_speed(-6*u, 4*u, 0, speed)
        tello.go_xyz_speed(3*u, -2*u, 0, speed)
    elif (digit == 8):
        tello.go_xyz_speed(0, 1*u, 0, speed)
        tello.go_xyz_speed(1*u, 1*u, 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(-1*u, 1*u, 0, speed)
        tello.go_xyz_speed(0, 2*u, 0, speed)
        tello.go_xyz_speed(-1*u, 1*u, 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(1*u, 1*u, 0, speed)
        tello.go_xyz_speed(0, 1*u, 0, speed)
    elif (digit == 9):
        tello.go_xyz_speed(1*u, -2*u, 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(-4*u, 0, 0, speed)
        tello.go_xyz_speed(3*u, 2*u, 0, speed)
    elif (digit == 0):
        tello.go_xyz_speed(3*u, 0, 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(1.5*u), 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(-2*u, 0, 0, speed)
        tello.go_xyz_speed(int(-1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(int(-0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(0.5*u), int(-1.5*u), 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(-0.5*u), 0, speed)
        tello.go_xyz_speed(2*u, 0, 0, speed)
        tello.go_xyz_speed(int(1.5*u), int(0.5*u), 0, speed)
        tello.go_xyz_speed(-3*u, 0, 0, speed)


tello = Tello()

tello.connect(True)

tello.streamon()

tello.takeoff()

tello.move_up(50)

ar = ArucoReader()

while True:
    frame = tello.get_frame_read().frame
    if frame is not None:
        markerData = ar.checkForArUco(frame)
        if markerData is not None:
            flyNumPattern(markerData[1][0][0], tello)
            break
    if (cv2.waitKey(1) == 27): break

tello.land()