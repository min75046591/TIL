"""
다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것.
모든 정점을 너비우선탐색 하여 경로를 출력.
시작 정점을 1로 시작
"""

"""
V E : V 1~V번 까지 V개의 정점. E개의 간선
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# 츨력결과 : 1 - 2 - 3 - 4 - 5 - 7 - 6

def bfs(s, N):              # 시작정점 s, 노드개수 N
    q = []                  # 큐
    visited = [0] * (N+1)   # visited
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문표시
    while q:                # 큐가 비워질 때까지... (남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할일...
        print(t)
        for i in adjl[t]:   # t에 인접인 정점
            if visited[i] == 0:  # 방문하지 않은 정점이면
                q.append(i)      # 인큐
                visited[i] = 1 + visited[t]  # 방문표시
        print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
# 인덱스 연산의 방법으로 2개의 쌍으로 읽는 방법 [1,2] [1,3] [2,4] ...
# for i in range(0, E*2, 2) 이렇게도 가능 -> n1, n2 = arr[i], arr[i+1]    
    n1, n2 = arr[i*2], arr[i*2+1] 
    adjl[n1].append(n2)
    adjl[n2].append(n1)   # 무향그래프

bfs(1, V)
