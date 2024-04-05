"""
탈주범은 시간당 1의 거리를 움직일 수 있음
중복 가능 -> 지나간 장소 다시 갈 수 있음, 한 자리에 계속 있을 수 있음
-> 지나갈 수 있는 곳은 다 세기
"""
from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j, s):
    # 종료 조건
    if s > L:  # 시간이 다 됐을 때
        return
    d = deque([i, j])
    visited[i][j] = 1    #  방문 표시

    while d:
        i, j = d.popleft()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]

            if cage[i][j] == 1:
            # 1. 상 (1, 2, 4, 7)일 경우에 가능
                if i-1 >= 0 and visited[i-1][j] == 0 and (cage[i-1][j] == 1
                                                       or cage[i-1][j] == 2
                                                       or cage[i-1][j] == 4
                                                       or cage[i-1][j] == 7):




        # 2. 하 (1, 2, 5, 6)일 경우에 가능


        # 3. 좌 (1, 3, 4, 5)일 경우에 가능


        # 4. 우 (1, 3, 6, 7)일 경우에 가능



T = int(input())
for tc in range(1, T+1):
    # 터널 지도의 세로 N, 가로 M, 맨홀 뚜껑이 위치한 장소의 세로 R, 가로 C, 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    cage = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0      # 탈주범이 위치 할 수 있는 장소의 개수
    bfs(R, C, 0)  # 시작 위치

    # 방문 위치 찾기
    for k in range(N):
        for l in range(M):
            if visited[k][l] > 0:
                cnt += 1

    print(f'#{tc} {cnt}')
