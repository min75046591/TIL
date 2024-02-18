def othello(i, j, bw):
    # 보드판에 돌 넣기
    map[i][j] = bw
    # 돌 뒤집기
    # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
    for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]:
        ni, nj = i + di, j + dj
        # 색이 다른 돌을 만날때까지 순회
        while 0 <= ni < N and 0 <= nj < N and map[ni][nj] == 3 - bw:
            ni, nj = ni + di, nj + dj
        # 색이 다른 돌 만났을 때 색이 다른 돌 뒤집기
        if 0 <= ni < N and 0 <= nj < N and map[ni][nj] == bw:
            ni, nj = i + di, j + dj
            # 현재 위치에 있는 돌이 상대 돌일때
            while 0 <= ni < N and 0 <= nj < N and map[ni][nj] == 3 - bw:
                map[ni][nj] = bw
                # 현재 위치에서 di dj 방향으로 이동
                ni, nj = ni + di, nj + dj

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 한변의 길이, M 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]
    map = [[0] * N for _ in range(N)]  # 오셀로 보드판

    # 시작 세팅
    # 흑돌
    map[N // 2 - 1][N // 2 - 1] = 1
    map[N // 2][N // 2] = 1
    # 백돌
    map[N // 2 - 1][N // 2] = 2
    map[N // 2][N // 2 - 1] = 2

    # 플레이 진행
    for i, j, color in play:  # 언패킹
        othello(i - 1, j - 1, color)  # 입력값을 인덱스 값에 맞게 변환

    # 색깔별 돌의 개수
    B = W = 0
    for k in range(N):
        for l in range(N):
            if map[k][l] == 1:
                B += 1
            elif map[k][l] == 2:
                W += 1

    print(f'#{tc} {B} {W}')
