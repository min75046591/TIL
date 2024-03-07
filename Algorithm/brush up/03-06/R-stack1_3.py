# 연습문제 3
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
def dfs(i, v):
    stack = []
    visited = [0] * (v+1)   # 1부터 마지막 노드까지 나타내기 위해 V+1
    print(i, end=' ')   # 시작점 출력
    visited[i] = 1      # 방문 표시
    while True:    
        for x in adjl[i]:   # i와 인접한 노드
            if visited[x]==0:
                print(x, end=' ')
                visited[x] = 1
                stack.append(i)     # 경로 i를 push
                i = x
                break
        else:   # 방문했던 곳이면
            if stack:
                i = stack.pop()
            else:
                return


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]     # 인접리스트
for i in range(E):  # 간선 수 만큼
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
dfs(1, V)