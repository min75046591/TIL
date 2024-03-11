T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리채 크기만큼 맵 순회 범위 정하기
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            for k in range(M):
                for l in range(M):
                    fly_sum += arr[i+k][j+l]

            if max_v < fly_sum:
                max_v = fly_sum
    print(f'#{tc} {max_v}')


