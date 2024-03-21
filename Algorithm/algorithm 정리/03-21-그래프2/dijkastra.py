import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

INF = int(1e9)  # 10억

V, E = map(int, input().split())
start = 0   # 시작 노드 번호

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    pq = []

    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # pq의 특성 때문에 더 긴 거리가 미리 저장되어 있음
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue


        # now 에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist  # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_dist, next_node))    # next_none 의 인접 노드들을 pq에 추가

dijkstra(0)
print(distance)