from collections import deque

def bfs(N, M):
    last = 0  # 마지막 토마토가 익은 순서
    q = deque()  # 큐생성
    visited = [[0] * M for _ in range(N)]  # visited 생성,토마토가 익은 순서
    cnt1 = 0  # 익은토마토 개수
    cnt2 = 0  # 빈칸 수
    for i in range(N):  # 시작점 인큐 - 익은 토마토의 위치
        for j in range(M):
            if tomato[i][j] == 1:  # 익은토마토==1
                q.append((i, j))
                visited[i][j] = 1  # 시작점 visited 표시
                cnt1 += 1
            if tomato[i][j] == -1:  # 빈칸 수
                cnt2 += 1
    if cnt1 + cnt2 == N * M:  # 익은토마토수+빈칸 == 전체격자
        return 0  # 이미 다 익은 상태 리턴
    while q:
        i, j = q.popleft()
        # i, j의 인접에 대해...(익은 토마토에 인접한 토마토가 있으면)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                last = visited[ni][nj]

    # 가능한 모든 토마토가 익었으면, 안익은 토마토 검사
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0 and visited[i][j] == 0:
                return -1  # 모두 익히는데 실패

    return last - 1  # 마지막으로 익는데 걸리는 시간


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M))