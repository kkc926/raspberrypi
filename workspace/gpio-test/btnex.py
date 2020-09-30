import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class BtnEx : 
    def __init__(self):
        self.led_pin = 18
        self.button_pin = 16
        

        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_pin,GPIO.OUT)

    def __call__(self):
        print("BtnEx call")
        while 1: #무한반복
        # 만약 버튼핀에 High(1) 신호가 들어오면, "Button pushed!" 을 출력합니다.
        # if GPIO.input(button_pin) == GPIO.HIGH:
        #     print("Button pushed!")
            GPIO.output(self.led_pin,GPIO.input(self.button_pin))
            time.sleep(0.1) # 0.1초 딜레이    #BtnEx클래스의 __call__() 메서드 호출 ex.__call__로 사용할 필요 없음