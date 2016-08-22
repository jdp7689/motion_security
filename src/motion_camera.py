#!/usr/bin/python

'''
MIT License
Copyright (c) 2016 Josh Palmer
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

import google_drive_helper
import motion_sensor
import time
from picamera import PiCamera
import os

class MotionCamera():
    def __init__(self):
        self.motion = motion_sensor.MotionSensor()
        self.camera = PiCamera()

    def start(self):
        while True:
            print "Waiting for motion..."
            self.motion.wait_for_motion(timeout=False) # Will wait here
            for i in xrange(2):
                time_string = time.strftime("%d%m%y%H%M%S")
                self.record_video_and_send(time_string)
            
    def record_video_and_send(preface_string, record_time=15):
        filename = preface_string + "_security_feed.h264"
        self.camera.start_recording(filename)
        sleep(record_time)
        self.camera.stop_recording()
        google_drive_helper.GoogleDriveHelper().upload_file(filename)
        print "Uploaded {} to Drive".format(filename)
        os.remove(filename)

def main():
    motion_cam = MotionCamera()
    motion_cam.start()
    

if __name__ == '__main__':
    main()
