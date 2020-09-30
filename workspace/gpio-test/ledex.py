import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class LedEx : 
    def __init__(self):
        self.led_pin =18
        GPIO.setup(self.led_pin,GPIO.OUT)

    def __call__(self):
        print("LED CALL 10회")
        for i in range(10):
            print(10-i)
            GPIO.output(self.led_pin,1) # LED ON
            time.sleep(1) # 1초동안 대기상태
            GPIO.output(self.led_pin,0) # LED OFF
            time.sleep(1) # 1초동안 대기상태

