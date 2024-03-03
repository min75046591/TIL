T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bd = [[0]*N for _ in range(N)]
    b = 1
    w = 2
    # 보드판 세팅
    bd[N//2-1][N//2-1] = w
    bd[N//2][N//2] = w
    bd[N//2-1][N//2] = b
    bd[N//2][N//2-1] = b

    for _ in range(M):
        j, i, wb = map(int, input().split())

        bd[i-1][j-1] = wb
        for di, dj in [[0, 1], [1, 0], [1, 1], [-1,-1], [-1, 1], [1, -1], [-1, 0], [0, -1]]:
            turn = []
            ni, nj = i-1+di, j-1+dj
            while 0 <= ni < N and 0 <= nj < N and bd[ni][nj] == 3-wb:
                turn.append((ni, nj))
                ni, nj = ni + di, nj + dj
            if 0 <= ni < N and 0 <= nj < N and bd[ni][nj] == wb:
                for g, v in turn:
                    bd[g][v] = wb

    cnt_b = 0
    cnt_w = 0

    for x in range(N):
        for y in range(N):
            if bd[x][y] == b:
                cnt_b += 1
            elif bd[x][y] == w:
                cnt_w += 1

    print(f'#{tc} {cnt_b} {cnt_w}')