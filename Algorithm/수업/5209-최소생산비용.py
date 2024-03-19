"""
한 곳당 한가지씩 생산
전체 제품의 최소 생산 비용을 계산
"""
def f(i, cost):
    global min_v
    if i == N:
        if min_v > cost:
            min_v = cost
            return
    if min_v < cost:
        return

    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            f(i+1, cost+arr[i][k])
            visited[k] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_v = 10000
    f(0, 0)
    print(f'#{tc} {min_v}')