T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    first = 0
    a = b = c = d = 0
# 왼쪽 위 모서리
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and first == 0:
                first += 1
                a, b = i, j


# 오른쪽 아래 모서리
    for k in range(N-1, -1, -1):
        for l in range(N-1, -1, -1):
            if arr[k][l] == 1 and first == 1:
                first += 1
                c, d = k, l


