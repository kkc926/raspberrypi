import time
import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 30
    camera.start_preview()
    # time.sleep(2)
    start_time=time.time()
    camera.capture_sequence([
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'image4.jpg',
        'image5.jpg',
        ],)
        # use_video_port=True)
    end_time=time.time()
    print(end_time - start_time)