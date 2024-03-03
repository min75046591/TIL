T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    w = 2
    b = 1
    # 보드 중앙에 기본값 설정
    arr[N//2-1][N//2-1] = w
    arr[N//2][N//2] = w
    arr[N//2-1][N//2] = b
    arr[N//2][N//2-1] = b

    for _ in range(M):
        j, i, wb = map(int, input().split())

        arr[i-1][j-1] = wb
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]:
            tmp = []
            ni, nj = i-1+di, j-1+dj
            while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 3-wb:
                tmp.append((ni,nj))
                ni, nj = ni+di, nj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == wb:
                for v, s in tmp:
                    arr[v][s] = wb

    cnt_b = 0
    cnt_w = 0
    for p in range(N):
        for q in range(N):
            if arr[p][q] == 1:
                cnt_b += 1
            elif arr[p][q] == 2:
                cnt_w += 1

    print(f'#{tc} {cnt_b} {cnt_w}')