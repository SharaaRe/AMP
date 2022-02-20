from RPi import GPIO


class LightingArmControl(GPIO):
    def __init__(self, input_devices, output_devices):
        raise NotImplementedError

    def calibrate(self, lights=False, swing_arm=False):
        raise NotImplementedError

    def switch_on(self):
        raise NotImplementedError

    def switch_off(self):
        raise NotImplementedError

    def right(self):
        raise NotImplementedError

    def left(self):
        raise NotImplementedError

    def to_home(self):  # TODO change the method name
        raise NotImplementedError

    def move_to(self, position, led_status=True):
        raise NotImplementedError
