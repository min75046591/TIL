"""
연습문제 3
모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오
시작 정점을 1로 시작
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

output
1 2 4 6 5 7 3
"""
def dfs(s, v):     # 시작점 s
    stack = []
    visited = [0] * (V+1)
    # 시작점 방문
    while True:        # 스택이 비워질 때 까지
        if visited[s] == 0:
            print(s, end=' ')
            visited[s] = 1
        for x in adjl[s]:   # i에 인접한 x
            if visited[x] == 0:     # 방문한 적이 없으면
                stack.append(s)     # 경로 i를 push하고
                s = x               # x로 이동
                break           # for x
        else:           # i에 인접한 정점이 더 이상 없으면
            if stack:       # pop()
                i = stack.pop()
            else:   # 스택이 비었으면
                return  # 중지


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]    # 인접 리스트
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

S = 1   # 시작점
dfs(S, V)