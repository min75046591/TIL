"""
청소하는 영역의 개수를 구하라

N * M 크기의 직사각형
바라보는 방향은 동:1, 서:3, 남:2, 북:0 중 하나
0이 청소되지 않은 빈 칸.
1은 벽
"""
di = [-1, 0, 1, 0]  # 북, 동, 남, 서
dj = [0, 1, 0, -1]  # 북, 동, 남, 서

def pipi(r, c, d):  # 시작 좌표 r,c / 방향
    global cnt
    arr[r][c] = 2  # 시작점 방문표시
    cnt += 1        # 방문 표시 후 cnt+1
    for i in range(N):
        for j in range(M):
            # 상, 우, 하, 좌
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                    d = abs(d-1)%4    # 반시계 방향으로 90도 회전
                    ni, nj = ni + di[d], nj + dj[d]
                    # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                        arr[i][j] = arr[ni][nj]    # 자리 이동
                        r, c = i, j
                        pipi(r, c, d)

                elif 0<=ni<N and 0<=nj<M and arr[ni][nj] != 0:
                    d = (d+2)%4 # 180도 회전
                    ni, nj = ni + di[d], nj + dj[d]
                    if arr[ni][nj] == 1:    # 벽이라 후진 할 수 없을 때
                        return

                    elif 0<=ni<N and 0<=nj<M and arr[ni][nj] != 1:
                        arr[i][j] = arr[ni][nj]
                        r, c = i, j
                        pipi(r, c, d)


N, M = map(int, input().split())        # 행, 열
r, c, dir = map(int, input().split())   # 처음에 있는 칸의 좌표, 방향
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0        # 청소한 구역
pipi(r, c, dir)
print(cnt)