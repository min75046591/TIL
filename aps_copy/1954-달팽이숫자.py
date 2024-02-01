T = int(input())
for tc in range(1, T + 1):
    # 배열의 크기
    N = int(input())
    # 맵 매트릭스
    matrix = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]  # 우 하 좌 상의 순서로 방향 전환
    dj = [1, 0, -1, 0]
    direction = 0
    input_v = 2
    i = j = 0
    matrix[i][j] = 1
    while input_v < N * N + 1:
        ni = di[direction] + i
        nj = dj[direction] + j
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


# 내꺼
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        # 좌표이동 - 우(0) 하(1) 좌(2) 상(3) = 시계방향
        snail = [[0] * N for _ in range(N)]  # 달팽이 맵
        di = [0, 1, 0, -1]  # 상 하
        dj = [1, 0, -1, 0]  # 좌 우
        input_v = 2
        dir = 0
        i = j = 0
        snail[i][j] = 1  # 0,0에서는 시작 숫자 1이 들어감

        while input_v < N ** N + 1:
            ni = i + di[dir]  # 다음 i축으로 이동할 방향과 거리
            nj = j + dj[dir]  # 다음 j축으로 이동할 방향과 거리
            if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:  # 이동값이 0이상 N미만이고 이동한 곳에 0일 있을때
                snail[ni][nj] = input_v
                i = ni
                j = nj
                input_v += 1
            else:
                dir = (dir + 1) % 4  # 상 하 좌 우를 인덱스 범위 이상으로 가지 않기 위해서.

        print(f'#{tc}')
        for i in range(N):
            print(*snail[i])