class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()  # 본인에게 인스턴스 변수가 없어서 본인이 만든 클래스로 올라가서 사용
p1.talk()

p2 = Person()
p2.name = 'kim'
p2.talk()

print(Person.name)  # 언노운
print(p1.name)  # 언노운
print(p2.name)  # kim

p2.ssafy = 11  
print(p2.ssafy) # 11  얘네는 별도의 독립적인 공간이기 때문에 아무런 상관없이 출력
