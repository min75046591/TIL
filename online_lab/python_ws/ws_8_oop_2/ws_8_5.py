class Cat:
    sound = '야옹'



class Dog:
    sound = '멍멍'


class Pet(Cat, Dog):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return(f'애완동물은 {super().sound} 소리를 냅니다.')

print(Pet())