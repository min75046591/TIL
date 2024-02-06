N = int(input())

result = 0
for i in range(N):
    tmp = sum(map(int, str(i)))   
    result = i + tmp

    if result == N:
        print(i)
        break
    
else:
    print(0)

# 207 + 2 + 1 + 6 = 216
'''
str(i): 정수 i를 문자열로 변환하여 각 자릿수를 문자로 나열합니다.
map(int, ...): 문자열 내 각 문자에 int 함수를 적용하여 각 문자를 해당하는 정수 값으로 변환합니다.
sum(...): 매핑된 정수 값들의 합을 계산합니다.
'''