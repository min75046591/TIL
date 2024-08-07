"""
보드는 4x4, 6x6, 8x8 크기

모든 게임 시작시
w b
b w
로 돌을 놓고 시작
b : 흑돌 , w : 백돌

흑부터 시작
자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을때만 돌을 놓을 수 있다
그 때의 상대 돌은 자신의 돌로 바뀐다

가로 / 세로 / 대각선 가능

돌을 놓을 수 없는 곳은 입력으로 주어지지 않음.

따라서

-출력-
흑돌과 백돌의 개수를 출력
"""


def othello(i, j, bw, N):
    # 보드판에 돌 넣기
    board[i][j] = bw
    # 돌 뒤집기
    # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상 검사
    for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]:
        ni, nj = i + di, j + dj
        tmp = []
        # 색이 다른 돌이면 계속 이동
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 3 - bw:
            tmp.append((ni, nj))
            ni, nj = ni + di, nj + dj

        # 다른 색 돌을 따라가다가 같은 색 돌을 만나면
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for k, l in tmp:
                board[k][l] = bw


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 한변의 길이, M 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]  # 오셀로 보드판

    # 시작 세팅
    # 흑돌
    board[N // 2 - 1][N // 2 - 1] = 1
    board[N // 2][N // 2] = 1
    # 백돌
    board[N // 2 - 1][N // 2] = 2
    board[N // 2][N // 2 - 1] = 2

    # 플레이 진행
    for i, j, color in play:  # 언패킹
        othello(i - 1, j - 1, color, N)  # 입력값을 인덱스 값에 맞게 변환

    # 색깔별 돌의 개수
    B = W = 0
    for k in range(N):
        for l in range(N):
            if board[k][l] == 1:
                B += 1
            elif board[k][l] == 2:
                W += 1

    print(f'#{tc} {B} {W}')