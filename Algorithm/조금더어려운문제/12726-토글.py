"""
N x N
1 -> 0 / 0 -> 1 로 바뀌는게 토글
각 칸의 숫자는 M초까지 1초마다 조건에 따라 토글됨

1) k초가 되는 순간, i+k 가 같거나 k의 배수가 되는 영역은 토글
2) M이 k의 배수인 경우와 M초에는 1)을 따르는 대신 전체가 토글

M초 후 1인 영역의 개수를 출력
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # M 몇초인지
    arr = [list(map(int, input().split())) for _ in range(N)]

    # i와 j가 같을때 -> 대각선

    # M이 K의 배수면