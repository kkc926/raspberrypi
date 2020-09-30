#!/usr/bin/python 
# 인터프리터의 경로 python Btn_Polling.1.py 를 하지 않아도됨. (CRLF->LF 변경해야함)

import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 16
led_pin = 18

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin,GPIO.OUT)
try:
    while 1: #무한반복
    # 만약 버튼핀에 High(1) 신호가 들어오면, "Button pushed!" 을 출력합니다.
    # if GPIO.input(button_pin) == GPIO.HIGH:
    #     print("Button pushed!")
        GPIO.output(led_pin,GPIO.input(button_pin))
        time.sleep(0.1) # 0.1초 딜레이

except KeyboardInterupt:
    GPIO.cleanup
