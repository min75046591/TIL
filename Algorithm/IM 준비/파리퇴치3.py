T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_f = 0

    for i in range(N):
        for j in range(N):
            # +로 분사
            sum_1 = arr[i][j]
            sum_2 = arr[i][j]
            for p in range(1, M):
                for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
                    ni, nj = i+di*p, j+dj*p
                    if 0<=ni<N and 0<=nj<N:
                        sum_1 += arr[ni][nj]
                if max_f < sum_1:
                    max_f = sum_1

            # x로 분사
                for di, dj in [[-1,-1], [-1,1], [1,1], [1,-1]]:
                    ni, nj = i + di * p, j + dj * p
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_2 += arr[ni][nj]

                if max_f < sum_2:
                    max_f = sum_2

    print(f'#{tc} {max_f}')