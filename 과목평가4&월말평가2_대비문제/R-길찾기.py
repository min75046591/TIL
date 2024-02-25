"""
A도시에서 B도시로 가는길이 존재하는지
최대 2개의 갈림길이 존재
모든 길은 일반통행이며 되돌아 오기 불가능
A : 0
B : 99
정점의 최대 개수 : 100개
"""
def dfs(a):          # 출발과 도착지
    stack = []
    visited[a] = 1      # 출발지 방문표시
    while True:
        for next in adj[a]:
            if visited[next] == 0:  # 방문한 곳이 0이라면
                stack.append(a)     # 스택에 a 넣기
                visited[next] = 1   #
                a = next
                break
        else:
            if stack:               # 스택에 요소가 남아있다면
                a = stack.pop()
            else:
                break

for p in range(10):
    tc, N = map(int, input().split())   # N 간선 개수
    arr = list(map(int, input().split()))
    A, B = 0, 99                          # 출발과 도착지
    visited = [0] * 100             # 방문 표시 리스트
    adj = [[] for _ in range(100)]  # 인접 리스트
    for i in range(N):
        n1, n2 = arr[2*i], arr[2*i+1]   # 왼쪽 자식 노드와 오른쪽 자식 노드
        adj[n1].append(n2)      # 부모 노드에 자식 노드의 값 넣기

    dfs(A)
    print(f'#{tc} {visited[B]}')