a = int(input(), 16)    # 16진수로 변환


print(a)

print(f'{a:X}')

print(f'{a:3X}')     # 문자로 변환 후 대문자로 출력

print(f'{a:04x}')     # 문자로 변환 후 소문자로 출력

#  round() 함수를 사용하여 3.5를 7로 나눈 후, 결과를 소수점 이하 둘째 자리까지 반올림하여 출력하는 것
print(round(3.5/7, 2)) 


# 소수점 둘째 자리까지 반올림하지 않고 출력
result = 3.5 / 7
print(f"{result:.2f}")

"""
input : A
output
A
10
A
  A
000a
0.5
"""