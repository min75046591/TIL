"""
n x n
동서남북

기지국으로 커버되지 않는 집의 수를 찾아라
A = 동서남북 1
B = 동서남북 2
C = 동서남북 3

집이 위치한 곳은 H
X인 원소는 아무것도 없다는 뜻
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):

            if arr[i][j] == 'A':
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                        arr[ni][nj] = 'X'


            if arr[i][j] == 'B':
                for p in range(1, 3):
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ni, nj = i + di*p, j + dj*p
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'


            if arr[i][j] == 'C':
                for p in range(1, 4):
                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ni, nj = i + di*p, j + dj*p
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'

    for k in range(N):
        for l in range(N):
            if arr[k][l] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')