# 시작점 찾기
def start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

# 미로 탈출
def escape(i, j, N): # i, j 시작점 / N 크기
    q = []                      # 큐 생성
    visited = [[0]*N for _ in range(N)]   # 방문 확인을 위한 리스트 생성
    q.append((i,j))                 # 시작지점 인큐
    visited[i][j] = 1              # 시작지점 방문표시
    while q:                        # 큐에 아무것도 없을때 까지
        i, j = q.pop(0)             # 방문 할 칸 디큐
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1   # 인큐 표시

        if maze[i][j] == '3':
            return visited[i][j] - 2

    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    str_i, str_j = start(N)

    print(f'#{tc} {escape(str_i, str_j, N)}')