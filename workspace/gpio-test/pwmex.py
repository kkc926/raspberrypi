import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class PwmEx : 
    def __init__(self):
        self.led_pin = 18
        

        GPIO.setup(self.led_pin,GPIO.OUT)
        self.p=GPIO.PWM(self.led_pin, 50)
        self.p.start(0)


    def __call__(self):
        print("PwmEx call")
        try:
            while 1:
                # fade in
                for dc in range(0,101,5):
                    self.p.ChangeDutyCycle(dc)
                    time.sleep(0.1) #아두이노 딜레이함수와 같은 역할(0.1초)

                # fade out
                for dc in range(100,-1,-5):
                    self.p.ChangeDutyCycle(dc)
                    time.sleep(0.1)


        except KeyboardInterrupt:
            self.p.stop()
    
