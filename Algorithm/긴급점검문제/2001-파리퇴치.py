T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # M 맵 길이, N 파리채 길이
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    # 파리 맵 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):

    # 파리채 내부 파리수 더하기
            sum_fly = 0
            for p in range(M):
                for q in range(M):
                    sum_fly += fly_map[i+p][j+q]

            if max_fly < sum_fly:
                max_fly = sum_fly

    print(f'#{tc} {max_fly}')