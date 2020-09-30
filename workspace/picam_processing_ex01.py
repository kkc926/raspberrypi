import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
   
    output = np.empty((240, 320, 3), dtype=np.uint8)
    while True:
        camera.capture(output, 'bgr',use_video_port=True)
        cv2.imshow('frame',output)
        key=cv2.waitKey(24)

        if key==27:
            break

    cv2.destroyAllWindows()