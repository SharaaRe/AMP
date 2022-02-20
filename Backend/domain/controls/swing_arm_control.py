from typing import List

from RPi import GPIO


# TODO methods need encapsulation to create a better interface, or create a higher level class for more abstraction

class SwingArmControl(GPIO):
    def __init__(self, pins: List):
        raise NotImplementedError

    def calibrate(self):
        raise NotImplementedError

    def move_right(self, speed):
        raise NotImplementedError

    def move_left(self, speed):
        raise NotImplementedError

    def move_to_location(self, location):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

# swing_arm_controller = SwingArmController(pins=pins)
