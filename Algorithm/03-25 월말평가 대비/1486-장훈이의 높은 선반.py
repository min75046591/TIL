"""
서점에 있는 점원의 수 N
각 점원의 키는 H.
점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 함
점원들이 쌓는 탑은 점원 1명 이상으로 이루어짐

탑의 높이가 B 이상인 경우 선반위의 물건 사용 가능.
탑의 높이가 B이상 중 탑의 높이와 B의 '차이'가 가장 작은 것을 출력
"""
import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, s):
    global min_v
    if s >= B:
        if s < min_v:
            min_v = s
            return

    if idx == N:
        return

    # 선택
    dfs(idx+1, s+arr[idx])
    # 선택 안함
    dfs(idx+1, s)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())        # 직원 수, 선반의 높이
    arr = list(map(int, input().split()))   # 직원들의 키
    min_v = 10001*N
    dfs(0, 0)
    print(f'#{tc} {abs(B-min_v)}')