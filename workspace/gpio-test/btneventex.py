import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class BtnEventEx : 
    def __init__(self):
        self.button_pin = 16
        self.led_pin = 18
        # 버튼 핀의 IN/OUT 설정 , PULL DOWN 설정
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.light_on=False
    
    def button_callback(self,channel):
        if self.light_on == False: # LED 불이 꺼져있을때
            GPIO.output(self.led_pin,1) # LED ON
            print("LED ON!")
        else: # LED 불이 져있을때
            GPIO.output(self.led_pin,0) # LED OFF
            print("LED OFF!")
        self.light_on = not self.light_on # False <=> True
    # Event 알림 방식으로 GPIO 핀의 Rising 신호를 감지하면 button_callback 함수를 실행
    # 300ms 바운스타임을 설정하여 잘못된 신호를 방지합니다.



    def __call__(self):
        print("BtnEventEx call")
        self.light_on=False
        GPIO.add_event_detect(self.button_pin,GPIO.RISING,callback=self.button_callback,bouncetime=50)
        try:
            while 1:
                time.sleep(0.1) # 0.1초 딜레이
        except KeyboardInterrupt:
            GPIO.remove_event_detect(self.button_pin)