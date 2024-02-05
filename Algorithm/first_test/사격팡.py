T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_map = [list(map(int, input().split())) for _ in range(N)]
    di = [0, -1, 0, 1]  # 상 하
    dj = [-1, 0, 1, 0]  # 좌 우
    
    max_v = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            temp = 0
            # 상하좌우의 값을 temp에 합산
            for k in range(4):
                temp += num_map[i+di[k]][j+dj[k]]
                
            # 합산한 결과에서 위치값은 뺀다
            sum_score = temp - num_map[i][j]

            if sum_score % 2 == 0:
                sum_score *= 2
            
            # 최대값 찾기
            if max_v < sum_score:
                max_v = sum_score
            

    # sum_list에 담겨있는 보너스 점수들 중 가장 큰 값 구하기
    
    print(f'#{tc} {max_v}')
