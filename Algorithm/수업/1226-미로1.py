"""
16*16형태 N = 16
가로 x
세로 y
시작점 (1,1)
도착점 (13,13)
"""
def bfs(i, j, N):
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append((i,j))         # 시작점 인큐
    visited[i][j] = 1       # 방문표시

    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))                  # 다음 칸 인큐
                visited[ni][nj] = visited[i][j] + 1     # 다음칸에 방문표시

    return 0

for tc in range(1, 11):
    T = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]

    str_i, str_j = 1, 1

    print(f'#{T} {bfs(str_i, str_j, N)}')