# 클래스 메서드 예시
class Person:
    count = 0

    def __init__(self, name):
        self.name =name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')


Person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population() # 인구수는 2입니다.