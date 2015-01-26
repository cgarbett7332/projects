import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 90
    camera.start_preview()
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_preview()
    camera.stop_recording()
