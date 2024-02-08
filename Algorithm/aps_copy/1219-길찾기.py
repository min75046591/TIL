def dfs(s, e):  # s 출발, e 도착
    visited = [0]*100   # visited, stack 생성 및 초기화
    stack = []
    visited[s] = 1      # 시작점 방문표시
    v = s               # 현재 방문 위치 v
    while True:         # 탐색
        for w in adjl[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[v] = 1
        else:       # 지나온 곳에서 다시 탐색
            if stack:       # 지나온 곳이 남아있다면
                v = stack.pop()
            else:       # 출발지까지 거슬러 와서 가능한 모든 곳을 확인한 경우
                break   # while True:
        if v == e:
            return 1
    return 0


for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjl = [[] for ]
    for i in range(0, E*2, 2):
        n1, n2 = arr[i], arr[i+1]   # n1 -> n2 도로가 있음
        if A[n1] == -1:
            A[n1] = n2
        else:
            B[n1] = n2
    print(f'#{tc} {dfs(0, 99)}')