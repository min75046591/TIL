def greet(name):
    """입력된 이름 값에
    인사를 하는 메세지를 만드는 함수
    """
    message = 'Hello' + (name)
    return message
# 함수 호출
result = greet('민')
print(result)


def greet(name, age = 30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('bob')  # 매개변수에 기본 인자 값을 넣지 않으면 아래처럼 나옴
# TypeError: greet() missing 1 required positional argument: 'age'

# 기본 인자 값 (Default Argument Values)
greet('Charlie', 40)
# 키워드 인자 (Keyword Arguments)
greet(name='joel', age=22)


def greet(name, age = 30):
    ex = (f'안녕하세요, {name}님! {age}살이시군요.')
    return ex

result = greet('민수', 26)
print(result)

print("-----")

# 임의의 인자 목록 -> 매개변수 앞에 '*'를 붙여 인자를 tuple로 처리
def caculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계 : {total}')

caculate_sum(1, 2, 3)

print("-----")
# 임의의 키워드 인자 목록 -> 매개변수 앞에 '**'를 붙여 사용 -> dictionary로 처리
def print_info(**info):
    print(info)

print_info(name='Eve', age=30)
print('\n')


def print_info(**info):
    return info

result = ('Eve', 30)
print(result)  # 이렇게 하면 딕셔너리 형태로 출력 안됨

print('-----')

# LEGB Rule 예시
a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)

    local(500)
    print(a, b ,c)

enclosed()
print(a, b)

print("-----")

# global 키워드
"""
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
"""
num = 0 # 전역 변수

def increment():
    global num # num을 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1

# global 주의사항
'''
- global 키워드 선언 전에 접근시 -> SyntaxError
- 매개변수에 global 사용 불가
 ex) def increment(num):  -> 'num' is assigned before global declaration

 -> global 키워드는 가급적 사용 x
 : 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 함수의 반환 값을 사용 권장
 '''

print('-----')

# 재귀 함수 예시 - 팩토리얼
def factorial(n):
    # factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n -1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result) # 120

'''
- 큰 문제를 작은 단위로 쪼개가면서 풀이할 때 쓰는 함수
- 종료 조건을 명확히 하지 않으면 무한회귀함. == while문
- 반복되는 호출이 종료 조건을 향하도록 해야함
'''

print('-----')
# map 함수 -> map(function, iterable(== sequence(문자열, 리스트, 튜플)))
'''python
numbers = input().split()

print(numbers) # ['1', '2', '3', '4', '5'] 스플릿 -> 띄어쓰기를 구분으로 나눠짐

result = map(int, numbers)
print(result)  # <map object at 0x00000117BEF3FB50>
print(list(result))  # [1, 2, 3, 4, 5]

result = list(map(int, input().split())) # 이런식으로 활요 가능
'''
print('-----')

# zip (*iterables) → 가연인자 가능 : 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)  # <zip object at 0x000001A5541F6800>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]

print('-----')

# lambda 함수
'''
- 간단한 연산이나 함수를 한 줄로 표현할 때 사용
- 함수를 매개변수로 전달하는 경우에도 유용하게 활용
'''
addition = lambda x, y: x + y

result = addition(3, 5)
print(result) # 8

print('\n')

numbers = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2 

result = list(map(func, numbers))
print(result)  # [1, 4, 9, 16, 25]

result_2 = list(map(lambda x: x ** 2, numbers))
print(result_2)  # [1, 4, 9, 16, 25]

print('-----')

# * 을 활용한 언패킹 -> 리스트의 요소를 언패킹
names = ['민수', '지훈', '민지']
print(*names) # 민수 지훈 민지


# ** 을 활용한 언패킹 -> 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹
def my_func(x, y, z):
    print(x, y ,z)

my_dict = {'x' : 1, 'y' : 2, 'z' : 3}
my_func(**my_dict)  # 1 2 3