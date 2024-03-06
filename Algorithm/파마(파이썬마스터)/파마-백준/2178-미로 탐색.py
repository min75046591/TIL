"""
N x M 배열
1은 이동, 0은 이동할 수 없는 칸
(1,1)에서 출발
(N,M) 도착
이동할 때 지나야 하는 최소의 칸 수를 구하라
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동 가능

칸을 셀 때에는 시작 위치와 도착 위치도 포함

"""
from collections import deque

def bfs(i, j):
    queue = deque()     # deque 라이브러리 사용
    queue.append((i, j))    # 현재 위치 추가
    while queue:    # queue 가 빌 때까지 반복
        i, j = queue.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 0:    # 맵을 나가지 않고 벽이 아닌 경우
                







N, M = map(int, input().split())
arr = [list(int(input())) for _ in range(N)]
i = j = 0   # 시작점
min_v = 10000   # 최소의 칸 수
arr[N-1][M-1] = 3   # 도착점 표시
# 방문하면서 1을 지우기
