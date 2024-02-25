def find_way(s, g):         # 출발점과 도착점을 인자로 받는 함수
    visited = [0] * (V+1)    # 방문 여부를 저장하는 리스트 초기화
    stack = []               # DFS를 위한 스택 초기화
    stack.append(s)          # 시작점을 스택에 넣기
    while stack:             # 스택에 요소가 있는 동안 반복
        node = stack.pop()   # 스택에서 노드를 하나 꺼내서 node에 저장
        if node == g:        # 노드가 도착지와 같다면
            return 1          # 경로가 존재하므로 1을 반환
        visited[node] = 1     # 방문한 노드를 표시
        for w in graph[node]:  # 현재 노드에 연결된 모든 노드에 대해
            if not visited[w]:  # 방문하지 않은 정점일 경우
                stack.append(w)  # 스택에 추가하여 탐색 계속 진행
    return 0                  # 모든 노드를 방문했지만 도착 노드에 도달하지 못한 경우 0을 반환


T = int(input())              # 테스트 케이스 개수 입력
for tc in range(1, T+1):       # 각 테스트 케이스에 대해 반복
    V, E = map(int, input().split())    # 노드 개수 V와 간선 개수 E 입력
    graph = [[0] for _ in range(V+1)]   # 그래프 초기화
    for i in range(E):          # 간선 정보 입력
        s_node, f_node = map(int, input().split())
        graph[s_node].append(f_node)  # 인접 리스트에 연결된 노드 추가

    S, G = map(int, input().split())    # 출발지와 도착지 입력
    result = find_way(S, G)             # find_way 함수 호출
    print(f'#{tc} {result}')           # 결과 출력