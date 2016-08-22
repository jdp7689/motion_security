#!/usr/bin/python

import RPi.GPIO as GPIO
import time

INPUT_PIN = 7
SLEEP_TIME_SECONDS = .1

class MotionSensorTimeoutException(Exception):
    pass


class MotionSensor():
    def __init__(self, input_pin=INPUT_PIN):
        self.input_pin = input_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(input_pin, GPIO.IN)

    def wait_for_motion(self, timeout=5.0):
        '''
        This is a blocking function

        param timeout: timeout in seconds. Set to false to block forever.
        '''
        curr_time = 0.0
        while True:
            #Raise exception for timeout
            if timeout is not False and float(curr_time)>timeout:
                raise MotionSensorTimeoutException
            elif GPIO.input(self.input_pin):
                break
            else:
                time.sleep(SLEEP_TIME_SECONDS)
            if timeout is not False:
                curr_time += SLEEP_TIME_SECONDS

def main():
    motion_sensor = MotionSensor()
    try:
        motion_sensor.wait_for_motion()
        print "Motion sensed!"
    except MotionSensorTimeoutException:
        print "No motion detected!"
if __name__ == "__main__":
    main()
