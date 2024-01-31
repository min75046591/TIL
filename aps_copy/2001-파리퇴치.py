T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())

    fly_map = [list(map(int, input().split())) for _ in range(N)]
    result_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            one_sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    one_sum += fly_map[k][l]
            result_list.append(one_sum)
        print()
    max_sum = 0
    for sum_v in result_list:
        if max_sum < sum_v:
            max_sum = sum_v

    print(f'#{tc} {max_sum}')
