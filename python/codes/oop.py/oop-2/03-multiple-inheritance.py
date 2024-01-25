class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Mom, Dad): # 중복된 속성이나 메서드는 상속 순서에 이해 결정됨
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'
    
baby1 = FirstChild('김민수')
print(baby1.swim())
print(baby1.cry())
print(baby1.walk()) # 아빠가 걷기 / 
print(baby1.gene)
