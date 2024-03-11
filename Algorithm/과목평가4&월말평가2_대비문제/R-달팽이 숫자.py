T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail_map = [[0] * N for _ in range(N)]
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    dir = 0
    i = j = 0
    for num in range(1, N*N+1):
        snail_map[i][j] += num
        ni, nj = i+di[dir], j+dj[dir]
        if 0<=ni<N and 0<=nj<N and snail_map[ni][nj] == 0:
            i, j = ni, nj

        else:
            dir = (dir+1) % 4
            i, j = i+di[dir], j+dj[dir]

    print(f'#{tc}')
    for p in snail_map:
        print(*p)