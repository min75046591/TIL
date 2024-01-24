# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def calculate_area(self):
        result = self.x * self.y
        return result


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)


class Shape2:
    def __init__(self, a, b):
        self.a =a
        self.b =b

    def calculate_area(self):
        result = self.a * self.b
        return result


shape1 = Shape2(4, 5)
area2 = shape1.calculate_area()
print(area2)