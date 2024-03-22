"""
N개의 자연수 중 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하라
중복 없음
"""
def dfs(idx, s):
    global cnt
    if s == K:      # 합이 K가 되면
        cnt += 1
        return

    if idx == N or s > K:   # 인덱스 범위를 초과하거나 합이 K를 초과하는 경우
        return

    # 현재 수를 선택
    dfs(idx+1, s+arr[idx])
    # 선택하지 않는 경우
    dfs(idx+1, s)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)   # 인덱스 0부터 시작하고, 합계는 0부터 시작
    print(f'#{tc} {cnt}')