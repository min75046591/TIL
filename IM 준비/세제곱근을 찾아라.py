"""
양의 정수 N에 대해 N = X**3 이 되는 양의 정수 X를 구하라
양의 정수 X를 출력
없다면 -1을 출력
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -1
    tmp = round(N ** (1/3))
    if tmp * tmp * tmp == N:
        result = tmp

    print(f'#{tc} {result}')