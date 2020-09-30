import RPi.GPIO as GPIO
import time

#callable class 해당클래스를 함수호출처럼 사용가능 조건은 __call__()메서드가 반드시 있어야함.
class BtnEx : 
    def __init__(self):
        pass

    def __call__(self):
        print("BtnEx call")



if __name__=="__main__":
    ex=BtnEx()      # BtnEx 인스턴스, 생성자 호출(동적할당 힙에 만들어짐)
    # BtnEx ex; 정적할당(파이썬은 정적할당 없음)
    # BtnEx *ex = new BtnEx(); 동적할당
    # ex.메서드()
    # ex.멤버
    # ex() 함수형태로 클래스의 인스턴스 호출 --> __call__()메서드가 정의되있어야함.
    ex()            #BtnEx클래스의 __call__() 메서드 호출 ex.__call__로 사용할 필요 없음