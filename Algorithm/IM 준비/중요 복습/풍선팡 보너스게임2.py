T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            sum_b = arr[i][j]
            for p in range(1, N):
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = i+di*p, j+dj*p
                    if 0<=ni<N and 0<=nj<N:
                        sum_b += arr[ni][nj]

            if max_v < sum_b:
                max_v = sum_b

    print(f'#{tc} {max_v}')