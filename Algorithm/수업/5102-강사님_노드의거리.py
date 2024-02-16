def bfs(s, N, G):              # 시작정점 s, 노드개수 N
    q = []                  # 큐 생성
    visited = [0] * (N+1)   # visited 생성
    q.append(s)             # 시작점 인큐 in queue
    visited[s] = 1          # 시작점 방문표시( 인큐 표시 )
    while q:                # 처리 안된 정점이 남아있으면
        t = q.pop(0)        # 처리할 정점 디큐
        if t == G:          # 도착 정점에 도착하면
            return visited[t] - 1 # 최단 경로 간선 (최단간선은 1빼줘야함) 최단 경로의 길이는 간선의 개수가 아니라 노드의 개수에서 1을 뺀 값
        for i in adjl[t]:         # t에 인접인 정점이
            if visited[i] == 0:   # 인큐되지 않았으면(처리된적이 없으면)
                q.append(i)       # 인큐
                visited[i] = visited[t] + 1  # 방문표시
    return 0  # G까지 경로가 없는 경우

    print(visited)
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V 노드의 개수, E 간선 개수
    # 인접리스트
    # 각 노드에 대한 빈 리스트를 갖는 리스트를 생성하는데, 이를 통해 각 노드의 이웃들을 나타내는 인접 리스트를 구현
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
    # 인덱스 연산의 방법으로 2개의 쌍으로 읽는 방법 [1,2] [1,3] [2,4] ...
    # for i in range(0, E*2, 2) 이렇게도 가능 -> n1, n2 = arr[i], arr[i+1]    
        n1, n2 = map(int, input().split())
        # 무향그래프
        adjl[n1].append(n2)   # 노드 n1과 연결된 노드들의 리스트에 n2를 추가
        adjl[n2].append(n1)   # 무향 그래프에서 간선은 방향이 없기 때문에 두 노드 모두에 대해 서로를 이웃으로 추가
    S, G = map(int, input().split())  # S 출발 노드, G 도착 노드

    print(f'#{tc} {bfs(S, V, G)}')