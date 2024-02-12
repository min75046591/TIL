T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            # 파리채 크기 만큼
            for k in range(i, i+M):
                for l in range(j, j+M):
                    fly_sum += fly_map[k][l]
            
            if max_sum < fly_sum:
                max_sum = fly_sum
    print(f'#{tc} {max_sum}')
