def dfs(i, V):
    stack = []
    visited = [0] * (V+1)
    while True:
        if visited[i] == 0:
            print(i, end = ' ')
            visited[i] = 1
        for x in adjl[i]:       # i에 인접한 x
            if visited[x]==0:   # 탐색한적이 없으면
                stack.append(i) # 경로 i를 push하고
                i = x           # x로 이동
                break           # for x
        else:                   # i인점한 정점이 더이상 없으면
            if stack:           # pop()
                i = stack.pop()
            else:               # 스택이 비었으면
                return          # 중지

V, E = map(int, input().split()) # V 마지막정점번호==정점개수, E 간선수
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]     # 인접리스트
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

dfs(1, V)