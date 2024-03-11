di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, -1, 1]
# 반대 돌의 색 1->2, 2->1
op = [0, 2, 1]  # 반대편 돌의 색 op[bw]

def f(i, j, wb, N):  # i, j 돌을 놓을 행, 열. wb 돌의 색, N 게임판 크기
    bd[i][j] = wb   # bd[i][j]에 wb 돌 놓기
    # 8개의 방향에 대해, 뒤집을 수 있는지 확인
    for k in range(8):
        flip = []           # 같은색 돌을 만나면 뒤집을 위치 저장
        #이동하는 방법들
        # i = di[k]*p
        # ni += di[k]
        ni, nj = i+di[k], j+dj[k]
        # ni, nj에 반대색 들어 있으면 이동
        while 0<=ni<N and 0<=nj<N and bd[ni][nj] == op[wb]:
            flip.append((ni, nj))       # 뒤집을 후보
            ni, nj = ni+di[k], nj+di[k] # 이동
        if 0<=ni<N and 0<=nj<N and bd[ni][nj] == wb:  # 같은 색을 만나서 중단된 경우
            for p, q in flip:       # 중간에 있는 돌 뒤집기
                bd[p][q] = wb

B = 1   # 흑돌
W = 2   # 백돌

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 보드 크기, M 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]  # # 열, 행, 돌 :돌을 놓는 정보 저장
    bd = [[0] * N for _ in range(N)]
    # for _ in range(M):
    #     i, j, color = map(int, input().split())

    # 4개의 돌 놓기
    bd[N//2-1][N//2-1] = W
    bd[N // 2 - 1][N // 2] = B
    bd[N // 2][N // 2 - 1] = B
    bd[N//2][N//2] = W

    for j, i, wb in play:
        f(i-1, j-1, wb, N)  # 돌을 놓는 함수, 입력은 인덱스 1부터, 처리는 인덱스 0부터

    cnt_b = cnt_w = 0
    for i in range(N):
        for j in range(N):
            if bd[i][j] == W:
                cnt_w += 1
            elif bd[i][j] == B:
                cnt_b += 1

    print(f'#{tc} {cnt_b} {cnt_w}')