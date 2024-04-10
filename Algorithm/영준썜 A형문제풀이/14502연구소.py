di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(lab, N, M):
    global maxV
    f = -1
    r = -1
    q = [0] * N*M*2 # 큐 생성
    visited = [[0]*M for _ in range(N)] # visited 생성
    for i in range(N): # 시작점 인큐 및 visited 표시
        for j in range(M):
            if lab[i][j]==2:
                r += 1
                q[r] = i
                r += 1
                q[r] = j
                visited[i][j] = 1
    while(f!=r): # 큐가 비어있지 않으면 반복
        f += 1 # 디큐
        i = q[f]
        f += 1
        j = q[f]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if lab[ni][nj]==0 and visited[ni][nj]==0: # 인접이면(빈공간이고 바이러스가 퍼지지 않았으면)
                    r += 1
                    q[r] = ni
                    r += 1
                    q[r] = nj
                    visited[ni][nj] = visited[i][j] + 1
    # 모든 칸에 대해 lab[i][j]와 visited[i][j]가 0인 칸 수를 maxV와 비교
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j]==0 and visited[i][j]==0:
                cnt += 1
    if maxV<cnt:
        maxV = cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
safe = []
for i in range(N):                          # 벽을 세우기 위해 통로 목록 생성
    for j in range(M):
        if lab[i][j]==0:
            safe.append((i, j))
maxV = 0
for i in range(len(safe)-2):                # 통로 중 2칸을 선택하는 조합
    for j in range(i+1, len(safe)-1):
        for k in range(j+1, len(safe)):
            lab[safe[i][0]][safe[i][1]] = 1
            lab[safe[j][0]][safe[j][1]] = 1
            lab[safe[k][0]][safe[k][1]] = 1
            bfs(lab, N, M)
            lab[safe[i][0]][safe[i][1]] = 0
            lab[safe[j][0]][safe[j][1]] = 0
            lab[safe[k][0]][safe[k][1]] = 0
print(maxV)