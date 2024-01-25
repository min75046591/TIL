class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id


class Student(Person):
    def __init__(self, name, age, number, email, student_id):  # 인자는 그대로 설정해야함
        super().__init__(self, name, age, number, email)  # 여기도 인자는 맞춰줘야함
        self.student_id = student_id
