T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    map_matrix = list(map(int, input().split()))
    count = 0
    for i in map_matrix:
        dj = [i, 0, -i, 0]  # 우로 이동. 좌로 이동
        for j in range(K):
            start = map_matrix[0]  # 시작 지점
            if map_matrix[i] > 0 # 이동한 연잎이 양수라면
                ni = map_matrix[i]
                map_matrix[i] = map_matrix[i+j]
                    count += map_matrix[i][j] # 이동한 연잎의 점수를 count에 추가
            elif map_matrix[i] < 0 # 이동한 연잎이 음수라면
                map_matrix[i] -= map_matrix[i]
                    count -= map_matrix[i]
        # 시작시 밟고 있는 연잎 제외
                sum_num -= map_matrix[0]


        # 연잎 범위를 벗어나는 경우 점프를 더 이상 하지 않음
        if nj > N:
            break

    print(f'#{tc} {sum_num}')









    print(f'#{tc} {}')