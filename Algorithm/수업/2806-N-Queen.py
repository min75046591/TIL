# 강사님 .ver

def f(i, N):        # i행에 퀸을 놓는 함수
    global cnt
    if i == N:
        cnt += 1
        return      # 모든 행에 퀸을 놓은 경우
    else:
        # i행 j열에 퀸을 놓을 수 있는 조건
        # j열에 다른 퀸이 없어야함. 왼쪽 위, 오른쪽 위 대각선 상에도 없어야 함
        for j in range(N):
            if check(i, j, N):  # 놓을 수 있으면
                bd[i][j] = 1
                f(i+1, N)       # 다음 행으로 이동
                bd[i][j] = 0    # i행에서 이전에 놨던 퀸 삭제

def check(i, j, N):
    di = [-1, -1, -1]    # 다른 퀸이 있는지 검사하는 방향
    dj = [-1, 0, 1]
    for k in range(3):  # 각 방향에 대해
        ni, nj = i+di[k], j+dj[k]
        while 0<=ni<N and 0<=nj<N:
            if bd[ni][nj] == 1:     # 퀸이 있으면
                return False        # 놓을 수 없는 자리
            ni += di[k]
            nj += dj[k]
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bd = [[0]*N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(f'#{tc} {cnt}')