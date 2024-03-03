T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_f = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            f_sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    f_sum += arr[k][l]
            if max_f < f_sum:
                max_f = f_sum

    print(f'#{tc} {max_f}')