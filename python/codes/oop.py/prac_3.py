class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
        print(self.name)
        

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('bts')


Person.number_of_population()