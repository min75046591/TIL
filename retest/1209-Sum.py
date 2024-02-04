for _ in range(1, 10+1):
    tc = int(input())
    matrix_map = [list(map(int, input().split())) for _ in range(100)]
    sum_li = []
    cross_one_sum = 0
    cross_two_sum = 0
    for i in range(len(matrix_map)):
        tmp_vertical_sum = 0
        tmp_horizontal_sum = 0
        for j in range(len(matrix_map[i])):
            tmp_vertical_sum += matrix_map[i][j]  # 열의 합
            tmp_horizontal_sum += matrix_map[j][i] # 행의 합
            if i == j:
                cross_one_sum += matrix_map[i][j]
            if i+j == 100-1:
                cross_two_sum += matrix_map[i][j]

        sum_li.append(tmp_horizontal_sum)
        sum_li.append(tmp_vertical_sum)
        sum_li.append(cross_one_sum)
        sum_li.append(cross_two_sum)
    max_v = 0s
    for one_sum in sum_li:
        if max_v < one_sum:
            max_v = one_sum
    print(f'#{tc} {max_v}')