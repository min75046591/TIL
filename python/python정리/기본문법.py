print(-2 ** 4)  # -16
print(-(2 ** 4))  # -16
print ((-2)**4)  # 16

print('------')

# 변수 double에는 값 20의 주소가 들어 있으니 여전히 20을 참조
number = 10
double = 2 * number
print(double)  # 20
number = 5
print(double)  # 20

print('------')

# 파이썬에서 진수 표현
print(0b10) # 2진수 -> 2
print(0o30) # 8진수 -> 24
print(0x10) # 16진수 -> 16

print('------')

# escape sequence
print('철수야 \'안녕\'')
print('이 다음은 엔터\n입니다.')

print('------')


#  문자열 슬라이싱
a = 'hello'
print(a[:-1])
print(a[::-1]) # 역순
print(a[::-2])

#문자열은 불변
# a[1] = 'h'    # TypeError: 'str' object does not support item assignment
print('------')

# 딕셔너리 = 순서 없음. key를 통해 value 접근 가능

my_dict = {'민수' : '고은', '토이푸들' : '뚜비', '숫자' : [1, 2, 3]}
print(my_dict['민수'])
print(my_dict['토이푸들'])
print(my_dict['숫자'])

# 값 변경
my_dict['토이푸들'] = '이뚜비'
my_dict['숫자'][0] = 0

print(my_dict['토이푸들'])
print(my_dict['숫자'])

print('------')

#  set (세트) = 순서와 중복이 없음. 변경 가능
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)
print(my_set_2)
print(my_set_3)

# set의 집합 연산
set_1 = {1, 2, 3}
set_2 = {3, 6, 9}

# 합집합
print(set_1 | set_2) # {1, 2, 3, 6, 9}

# 차집합
print(set_1 - set_2)  # {1, 2}

# 교집합
print(set_1 & set_2)  # {3}

print('-----')

# boolean(불리언) = 비교 / 논리 연산의 평가 결과로 사용됨. 주로 조건/반복문과 사용
bool_1 = True
bool_2 = False

print(bool_1)
print(bool_2)
print(3 > 1)  # 불을 사용하지 않아도 파이썬 내부에서 판단해 True / False를 말해줌
print('3' != 3) # 정수형과 문자형은 다르기 때문에 같지 않다. -> True
print("3" == 3)
print(3 == 3)

print('-----')

print(1 == True) # True
print(1 is True) # False
