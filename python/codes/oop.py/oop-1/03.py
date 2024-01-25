class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2


class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r


c1 = Circle(5)
c2 = Circle(10)
