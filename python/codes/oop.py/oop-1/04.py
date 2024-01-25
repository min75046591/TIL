class Person:
    def __init__(self):
        print('인스턴스가 생성되었습니다.')


person1 = Person()  # 인스턴스가 생성되었습니다.


class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성되었습니다. {name}')


person1 = Person('지민')  # 인스턴스가 생성되었습니다. 지민
