class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

person1 = Person('민수')
person2 = Person('지훈')

print(Person.count)  # 2
print(person1.name)  # 민수