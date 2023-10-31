from djitellopy import Tello

tello = Tello()

tello.connect(True)

tello.takeoff()

tello.move_forward(75)

tello.land()