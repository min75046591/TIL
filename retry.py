T = int(input())
for tc in range(1, T+1):
    # 배열의 크기
    N = int(input())
    # 맵 매트릭스
    matrix = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0
    input_v = 2
    i = j = 0
    matrix[i][j] = 1

    while input_v < N * N + 1:
        ni = di[direction] + i
        nj = di[direction] + j
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0:
            matrix[ni][nj] = input_v
            i = ni
            j = nj
            input_v += 1
        else:
            direction = (direction + 1) % 4
    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])