from balloonIdentifier import BalloonIdentifier
from balloonTracker import BalloonTracker
from djitellopy import Tello
import cv2
import time
import threading

class Drone:
    
    serialNumber = ""

    ballIdentifier = None
    ballTracker = None
    tello = None

    def __init__(self, droneSerialNum : str, markerSize : float) -> None:
        self.serialNumber = droneSerialNum
        self.tello = Tello()

        self.ballIdentifier = BalloonIdentifier()
        self.ballTracker = BalloonTracker(self.serialNumber, markerSize)
        self.dx = 0.0
        self.dy = 0.0

    def spin(self):
        self.tello.send_rc_control(0,0,0,30)
        time.sleep(11)
        self.tello.send_rc_control(0,0,0,30)
        time.sleep(11)
        self.tello.send_rc_control(0,0,0,0)
        

    def spinSearch(self):
        spinThread = threading.Thread(target=self.spin)

        spinThread.start()

        while spinThread.is_alive():
            image = self.tello.get_frame_read().frame
            self.ballTracker.updateBalloonList(self.ballIdentifier.identifyBalloon(image), self.dx, self.dy, self.tello.get_yaw())
            cv2.imshow("image", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            cv2.waitKey(10)
        self.resetYaw()

    def resetYaw(self):
        yaw = self.tello.get_yaw()
        if yaw < 0:
            self.tello.rotate_clockwise(-yaw)
        elif yaw > 0:
            self.tello.rotate_counter_clockwise(yaw)

    def moveDrone(self, ddx, ddy):
        self.tello.go_xyz_speed(ddy, ddx, 0, 70)
        self.dx += ddx
        self.dy += ddy

    def goTo(self, dx, dy):
        self.tello.go_xyz_speed(int(dy - self.dy), int(dx - self.dx), 0, 70)
        self.dx = dx
        self.dy = dy

    def doTask(self):
        self.tello.connect(True)

        self.tello.streamon()

        # Wait for camera to stop malfunctioning
        while self.tello.get_frame_read().frame is None:
            time.sleep(1)

        self.tello.takeoff()
        self.tello.move_up(70)
        self.spinSearch()

        self.tello.land()
        self.tello.streamoff()

        self.ballTracker.printBalloonList()

drone = Drone("FC", 8)
drone.doTask()