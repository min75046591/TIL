"""
N개의 수로 이루어진 수열 -> 최대 10개
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자. 연산자는 +, -, *, /
수와 수 사이에 연산자를 하나씩 넣어 수식을 만들 수 있다.
주어진 수의 순서를 바꾸면 안됌

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행!
나눗셈은 정수 나눗셈으로 몫만 취함
음수를 양수로 나눌 때는 C++14의 기준을 따름 -> 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈

결과의 최대와 최소를 구하라!
"""
N = int(input())
nums = list(map(int, input().split()))
plus, minus, multip, divi = map(int, input().split())
i = nums[0]     # 첫번째 피연산자
max_v = 0       # 최대 값
min_v = 10000   # 최소 값
for j in range(1, N):
    sum_v = 0           # 어차피 연산은 연산자의 우선순위와 상관없이 앞에서부터 시작
    # 음수를 양수로 나눌 경우
    if i < 0:   # i가 음수일 경우


    if multip > 0:      # 곱하기 연산자가 1개 이상 있을 때
        sum_v = i * nums[j]
        multip -= 1     # 사용후 1개 차감
        i = sum_v       # 연산 후 i 를 연산 후 값으로 변경

    max_v = max(max_v, sum_v)
    min_v = min(min_v, sum_v)

print(max_v)
print(min_v)
