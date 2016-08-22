#!/usr/bin/python

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
