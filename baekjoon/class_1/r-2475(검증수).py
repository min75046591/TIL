num = map(int, input().split())

# 제곱한 수의 합을 저장할 result를 초기화
result = 0

for i in num:
    result += i**2

print(result%10)