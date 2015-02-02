import picamera
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 14
balloon = 2
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(balloon, GPIO.OUT)
print("Ready...")
GPIO.wait_for_edge(button, GPIO.FALLING)
GPIO.output(balloon, True)
sleep(5)
GPIO.output(balloon, False)
print("POP!")


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 90
    camera.start_preview()
    camera.start_recording('Balloon_Popping.h264')
    camera.wait_recording(60)
    camera.stop_preview()
    camera.stop_recording()
