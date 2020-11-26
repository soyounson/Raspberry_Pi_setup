import picamera
import time
import datetime

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    now = datetime.datetime.now()
    camera.start_recording(output = 'test.h264')
    camera.wait_recording(3)
    camera.stop_recording()