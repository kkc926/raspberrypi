import cv2
# cap = cv2.VideoCapture('http://172.30.1.58:4747/mjpegfeed')  # droid cam
cap = cv2.VideoCapture('./data/vtest.avi')  # 동영상(사운드는 지원 안됨.)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)
while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval: break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25) #25ms 대기, 초당 frame=40 ==>fps(frame per second)
    if key == 27: break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()