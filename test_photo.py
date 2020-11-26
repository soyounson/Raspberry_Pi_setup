import picamera
import time
import datetime

with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    now = datetime.datetime.now()
    camera.start_preview()
    time.sleep(2)
    camera.stop_preview()
    camera.capture('test.jpg')