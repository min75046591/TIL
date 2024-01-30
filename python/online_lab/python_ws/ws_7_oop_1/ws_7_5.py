# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'Shape: width={self.x}, height={self.y}'

shape1 = Shape(5, 3)
print(shape1)
