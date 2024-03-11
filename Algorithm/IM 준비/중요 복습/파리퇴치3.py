T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    # X자
    for i in range(N):
        for j in range(N):
            sum_f = arr[i][j]
            for p in range(1, M):
                for di, dj in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                    ni, nj = i+di*p, j+dj*p
                    if 0<=ni<N and 0<=nj<N:
                        sum_f += arr[ni][nj]

                    if max_v < sum_f:
                        max_v = sum_f

    # +자
    for i in range(N):
        for j in range(N):
            sum_ff = arr[i][j]
            for p in range(1, M):
                for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    ni, nj = i+di*p, j+dj*p
                    if 0<=ni<N and 0<=nj<N:
                        sum_ff += arr[ni][nj]

                    if max_v < sum_ff:
                        max_v = sum_ff

    print(f'#{tc} {max_v}')