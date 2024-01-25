# name = "Minsu"

# print(type(name))  # <class 'str'>

# print(help(str))

class Animal:

    def __init__(self, name):
        self.name = name

    def walking(self):
        return f'{self.name}가 걸어갑니다.'
    
    def running(self):
        return f'{self.name}가 뛰어갑니다'


animal1 = Animal('강아지')
print(animal1.walking())

animal2 = Animal('고양이')
print(animal2.walking())

animal3 = Animal('호랑이')
print(animal3.running())
