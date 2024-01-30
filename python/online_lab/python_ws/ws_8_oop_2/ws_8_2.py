# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        num_of_animal = 0


class Dog(Animal):
    def bark(self):
        super().__init__()
        print('멍멍 !')

dog1 = Dog()
dog1.bark()
