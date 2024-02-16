# 노드의 거리
def bfs(s, v, g):  # S 출발점, V 노드 개수, G 도착점
    q = []  # 큐 생성
    visited = [0]*(v+1)  # 방문 visited 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시 (인큐 표시)
    while q:  # 처리 안된 정점이 있다면~
        t = q.pop(0)  # 처리할 정점 디큐 delete queue
        if t == g:  # 도착 정점에 도착하면
            return visited[t]-1  # 최단 경로 간선 리턴

        for j in adjl[t]:   # t에 인접인 정점이
            if visited[j] == 0:  # 인큐되지 않았으면
                q.append(j)  # 인큐 해준다 q.append()
                visited[j] = visited[t] + 1    # 방문표시 해주기
    return 0  # 도착지점까지 경로가 없으면 리턴 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V+1)] # 노드의 개수 만큼
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, V, G)}')