# Module(모듈, 파이썬 표준 라이브러리) / Control of flow (제어문, 조건문, 반복문)

# Module(모듈) : 한 파일로 묶인 변수와 함수의 모음 == (.py)특정한 기능을 하는 코드가 작성된 파이썬 파일
# 내장 함수 help()를 사용하면 모듈에 무엇이 들어있는지 확인 가능

# math 모듈 : 파이썬이 미리 작성해 둔 수학 관련 '변수'와 '함수'가 작성된 모듈
import math

# 모듈명.변수명
# math.pi -> math 라는 모듈에서 pi라는 변수를 찾아라
print(math.pi)  # 3.141592653589793
print(math.sqrt(4)) # 2.0

print('\n')
# from 절 : 특정 모듈을 미리 참조하고 어떤 요소를 import할지 명시
from math import pi, sqrt

print(pi)  # 3.141592653589793
print(sqrt(16))  # 4.0

# 주의사항
'''
- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
-> 마지막에 import된 이름으로 대체

- 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음
-> from math import *
'''
print('\n')
# 직접 정의한 모듈 사용하기

# my_math.py
def add(x, y):
    return x + y

# Importing the module
import my_math

print(my_math.add(1, 2))

# 함수 표준 라이브러리
# 함수 < 모듈 < 패키지 < 라이브러리

# Package(패키지) : 관련된 모듈들을 하나의 디렉토리에 모아 놓은 것

# PSL 내부 패키지 -> 설치 없이 바로 import하여 사용
# 외부 패키지 -> pip를 사용하여 설치 후 import 필요
# pip : 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템

print('-----')

# 조건문 (Conditional Statement) : if / elif / else
a = 5

if a > 3:
    print('3 초과')
else:
    print('3 이하')

    print(a)  # 3 초과
'''
print(a) -> 초과 \n 5
'''
print('-----')

dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

# 매우 나쁨
# 위험해요! 나가지 마세요!

print('-----')

# 반복문 (Loop Statement)
'''
1. 특정 작업을 반복적으로 수행
2. 주어진 조건이 참인 동안 반복해서 실행
3. for / while -> 끝을 알면 for, 끝을 모르면 while
'''

# for: (str, tuple, list, range)의 항목들을 그 시퀀스에 들어있는 순서대로 반복
# for 변수 in 반복 가능한 객체:
# 반복 가능한 객체에는 dict, set도 사용 가능

# for _ in : 더미 변수 -> 많이 사용함
# (문자열 순회)
sample = 'apple'
for i in sample:
    print(i)
'''
a
p
p
l
e
'''
# apple이 'apple'길이 만큼 반복
print('-----')
sample = ['apple']
for _ in sample:
    print(_)
'''
apple
'''

print('-----')

items = ['apple', '민수', '지훈']

for item in items:
    print(item)

'''
apple
민수
지훈
'''

print('-----')

# range 순회
for i in  range(5):
    print(i)
'''
0
1
2
3
4
'''
print('-----')

# 딕셔너리 순회
my_dict = {
    'x' : 10,
    'y' : 20,
    'z' : 30,
}

for key in my_dict:
    # 딕셔너리는 그냥 뽑으면 key만 나옴
    print(key) # x\n y\n z -> key만 나옴
    # 딕셔너리의 key에 접근해서 value값 추출
    print(my_dict[key]) # 10\n 20\n 30 -> value만 나옴
'''
x
10
y
20
z
30
'''
print('-----')

# 인덱스로 리스트 순회
# 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경
numbers = [4, 6 ,10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
# [8, 12, 20, -16, 10] 

number = [4, 6, 10, -8, 5]

for i in number:
    i = number * 2

print(i)
'''
 [4, 6, 10, -8, 5, 4, 6, 10, -8, 5]
'''

print('-----')

# 중첩된 반복문
outers = ['A', 'B']
inners = ['C', 'D']

for outer in outers:
    for inner in inners:
        print(outer, inner)
# print가 호출되는 횟수 -> len(outers) * len(inners)

'''
A C
A D
B C
B D
'''
print('\n')
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)
'''
['A', 'B']
['c', 'd']
'''

print('-----')

elements = [['A', 'B'], ['c', 'd']]
    
for elem in elements:
    for item in elem:
        print(item)

'''
A
B
c
d
'''
print('-----')
# while : 조건식이 참 인동안 반복해서 실행.
# 조건식이 False가 될 때 까지 반복

numbers = [1, 3, 5 ,6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다') 

# 첫 번째 짝수를 찾았습니다: 6
print('-----')

# 프로그램 종료 조건 만들기
# number = int(input('양의 정수를 입력해주세요. :'))

# while number <= 0:
#     if number == -9999:
#         print('프로그램을 종료합니다.')
#         break

#     if number < 0:
#         print('음수를 입력했습니다.')
#     else:
#         print('0은 양의 정수가 아닙니다.')

#     number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')

print('-----')

# continue
# 홀수만 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = []
for num in range(len(numbers)):
    if num % 2 == 0:
        continue
    result_list.append(num)

print(result_list) # [1, 3, 5, 7, 9]

print('-----')

# List Comprehension 활용
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)

# 사용 후
numbers = [1, 2, 3, 4, 5]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# 리스트 컴프리헨션과 if 조건문
result = [i for i in numbers if i % 2 == 1]
print(result)  # [1, 3, 5]

result = []
for i in range(10):
    if i % 2 == 1:
        result.append(i)
print(result)  # [1, 3, 5, 7, 9]

# 컴프리헨션을 남용하지 말자. 간결한게 복잡할 수 있다.
print('-----')

# enumerate : iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')
'''
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
'''
fruits = ['apple', 'banana', 'cherry']
for i in enumerate(fruits):
    print(i) 
# (0, 'apple')
# (1, 'banana')
# (2, 'cherry')
    

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index)
'''
0
1
2
'''

fruits = ['apple', 'banana', 'cherry']
print(fruits[1]) # banana


fruits = ['apple', 'banana', 'cherry']
fruits_index = []
for index, fruit in enumerate(fruits):
    fruits_index.append(index)

print(fruits_index)  # [0, 1, 2]