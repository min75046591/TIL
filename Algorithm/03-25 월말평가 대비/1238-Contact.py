import sys
sys.stdin = open("input.txt", "r")

def bfs(start):
    global max_v
    visited = [0]*101
    q = [start]
    visited[start] = 1
    cnt = 1     # 가장 깊은 깊이 저장

    while q:
        now = q.pop(0)  # 현재 위치
        for next in graph[now]:
            if visited[next]:       # 이미 방문한 노드는 pass
                continue
            visited[next] = visited[now] + 1    # 가중치 +

            if cnt < visited[next] or (cnt == visited[next] and max_v < next):
                cnt = visited[next]
                max_v = next

            q.append(next)
    return max_v


for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = arr[i]
        e = arr[i+1]
        graph[s].append(e)                  # 인접리스트[시작]에 도착노드들 넣기
    max_v = 0
    bfs(start)

    print(f'#{tc} {max_v}')