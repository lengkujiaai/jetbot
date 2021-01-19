import Jetson.GPIO as GPIO
from traitlets.config.configurable import SingletonConfigurable
import time

class Pwm(SingletonConfigurable):
    pin_num = 37
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_num, GPIO.OUT, initial=GPIO.LOW)
    turn_left = 0.00085 #min value
    turn_middle = 0.00125
    turn_right = 0.00165 #max value

    def switch(self, high_time, angle=40):
        for i in range(angle):
            GPIO.output(self.pin_num, GPIO.HIGH)
            time.sleep(high_time)
            GPIO.output(self.pin_num, GPIO.LOW)
            time.sleep(0.020-high_time)


