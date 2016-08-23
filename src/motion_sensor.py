#!/usr/bin/python

'''
MIT License
Copyright (c) 2016 Joshua Palmer
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import RPi.GPIO as GPIO
import time

INPUT_PIN = 7
SLEEP_TIME_SECONDS = .1

class MotionSensorTimeoutException(Exception):
    """
    Exception for if we timeout
    """
    pass


class MotionSensor():
    """
    Class for initialzing a motion sensor on the Pi
    """
    def __init__(self, input_pin=INPUT_PIN):
        """
        :param input_pin: The input pin for reading the motion sensor
        """
        self.input_pin = input_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(input_pin, GPIO.IN)

    def wait_for_motion(self, timeout=5.0):
        """
        Blocks until the motion sensor line goes high. Will raise MotionSensorTimeoutException if there is a timeout

        :param timeout: (float) timeout, or -1 for no timeout
        :return: None
        """
        curr_time = 0.0
        while True:
            #Raise exception for timeout
            if timeout > 0 and float(curr_time) > timeout:
                raise MotionSensorTimeoutException
            elif GPIO.input(self.input_pin):
                break
            else:
                time.sleep(SLEEP_TIME_SECONDS)
            if timeout > 0:
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
