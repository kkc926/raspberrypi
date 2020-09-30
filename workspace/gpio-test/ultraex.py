import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class UltraEx : 
    def __init__(self):
        self.TRIG = 23
        self.ECHO = 24

        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)



    def __call__(self):
        print("UltraEx call")
        GPIO.output(self.TRIG, 0)
        print("Waiting for sensor to settle")
        time.sleep(2)
        
        try:
            while True:
                GPIO.output(self.TRIG, True) # Triger 핀에 펄스신호를 만들기 위해 1 출력
                time.sleep(0.00001) # 10µs 딜레이
                GPIO.output(self.TRIG, False)

                while GPIO.input(self.ECHO)==0:
                    start = time.time() # Echo 핀 상승 시간
                while GPIO.input(self.ECHO)==1:
                    stop= time.time() # Echo 핀 하강 시간

                check_time = stop - start
                distance = check_time * 34300 / 2
                print("Distance : %.1f cm" % distance)
                time.sleep(0.4) # 0.4초 간격으로 센서 측정

        except KeyboardInterrupt:
            print("Measurement stopped by User")
            GPIO.cleanup()

