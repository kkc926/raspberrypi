from piapp import *
import RPi.GPIO as GPIO
from ledex import LedEx
from btnex import BtnEx
from btneventex import BtnEventEx
from pwmex import PwmEx
from pwmservoex import PwmServoEx
from ultraex import UltraEx
from mcpex import McpEx

class GpioApp(PiApplication):
    def __init__(self):
        super().__init__()

    def create_menu(self,menu):
        #1. LED
        #2. 버튼
        #3. 버튼 이벤트(LED 켜고 끄기)
        
        menu.add_menu(MenuItem("종료",self.exit))  
        menu.add_menu(MenuItem("LED",LedEx())) #action = LedEx() 클래스를 매개변수 action으로 받음. action()를 하여 LedEx의 __call__()을 실행시킴
        #menu.add_menu(MenuItem("출력문",호출할 함수))
        menu.add_menu(MenuItem("Button",BtnEx()))
        menu.add_menu(MenuItem("Button Event",BtnEventEx()))
        menu.add_menu(MenuItem("Pwm Event",PwmEx()))
        menu.add_menu(MenuItem("PwmServo",PwmServoEx()))
        menu.add_menu(MenuItem("Ultra",UltraEx()))
        menu.add_menu(MenuItem("조도",McpEx()))
           

if __name__ == "__main__":
    app=GpioApp()
    app.run()