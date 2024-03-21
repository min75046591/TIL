# 강사님 dfs .ver
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    visited = [[int(1e9)] * N for _ in range(N)]    # visited[i][j] i, j칸까지의 연료소비량
    visited[0][0] = 0

    # 도착 비용이 갱신되는 칸을 인큐, 중복될 수 있음
    q = deque()         # 큐 생성, 비용이 갱신된 칸의 인접 인큐 (1칸의 주변도 다시 갱신 될 수 있으므로)
    q.append((0,0))
    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                diff = H[ni][nj] - H[i][j] if H[ni][nj] >= H[i][j] else 0 # 높이 차이에 의한 연료소비
                if visited[ni][nj] > visited[i][j] + diff + 1:        # 기존보다 연료를 덜 소비하고 도착하면
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + diff + 1          # ni, nj까지 새로운 연료소비량

    print(f'#{tc} {visited[N-1][N-1]}')

