T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        arr[ni][nj] = 'X'

            elif arr[i][j] == 'B':
                for p in range(1, 3):
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = i + di*p, j + dj*p
                        if 0 <= ni < N and 0 <= nj < N:
                            arr[ni][nj] = 'X'

            elif arr[i][j] == 'C':
                for p in range(1, 4):
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = i + di*p, j + dj*p
                        if 0 <= ni < N and 0 <= nj < N:
                            arr[ni][nj] = 'X'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')