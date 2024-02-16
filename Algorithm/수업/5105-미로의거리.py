"""
NxN 미로에서 최소 몇 개의 칸을 지나면 도착할 수 있는지
경로가 있으면 최소한의 칸 수
없으면 0을 출력 return 0
1은 벽. 0은 통로.
출발 : 2
도착 : 3
"""
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

def bfs(i, j, N):   # i, j 탐색시작위치, N크기
    q = []                                  # 큐 생성
    visited = [[0]*N for _ in range(N)]     # visited 생성
    q.append((i,j))                         # 시작점 인큐
    visited[i][j] = 1                       # 시작점 방문표시
    while q:                                # 남은 칸이 있으면
        i, j = q.pop(0)                     # 방문할 칸 디큐
        if maze[i][j] == '3':               # 목적지에 도착
            # 2를 빼는 이유는 출발점과 도착점에 각각 1씩 더해져 있기 때문
            return visited[i][j]-2
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]: # i,j에 인접하고, 방문하지 않은 경우(큐에 들어있지 않으면)
            ni, nj = i+di, j+dj                         # 인접 후보위치
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != '1' and visited[ni][nj]==0: # 인접조건 and 큐에 들어있지 않으면
                q.append((ni,nj))                           # 인큐
                visited[ni][nj] = visited[i][j] + 1         # 인큐 되었음 표시
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    sti, stj = find_start(N)

    result = bfs(sti, stj, N)
    print(f'#{tc} {result}')


#ver.2 - 내꺼
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