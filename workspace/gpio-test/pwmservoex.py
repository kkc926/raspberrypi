import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class PwmServoEx : 
    def __init__(self):
        self.led_pin = 25
        

        GPIO.setup(self.led_pin,GPIO.OUT)
        self.servo=GPIO.PWM(self.led_pin, 50)
        self.servo.start(0)


    def __call__(self):
        print("PwmServoEx call")
        try:
            while 1:
                self.servo.ChangeDutyCycle(7.5) # 90도
                time.sleep(1)
                self.servo.ChangeDutyCycle(12.5) # 180도
                time.sleep(1)
                self.servo.ChangeDutyCycle(2.5) # 0도
                time.sleep(1)


        except KeyboardInterrupt:
            self.servo.stop()
    
