from djitellopy import Tello

tello = Tello()

tello.connect(True)

tello.takeoff()

tello.move_forward(50)
tello.move_back(50)

tello.land()