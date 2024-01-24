class add_cal:
    
    def __init__(self, start):
        self.start = start 
        print("init function runned")

    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2
    

cal_1 = add_cal(0)
# add_cal.add(cal_1, 0, 3)
# print(cal_1.add(0,3))
# 호출방법 1 클래스이름, 인스턴스이름(self, 인자)
# class를 선언하고 인스턴스를 만들면서 동시에 데이터값을 주고싶을때
# __init__ 함수를 사용한다. 모든 개발자들이 사용함. 긍께 너도 사용해라

print(cal_1.start)