import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def prim(start):
    pq = []
    MST = [0] * (V+1)       # visited
    sum_weight = 0      # 최소 비용

    heappush(pq, (0, start))    # 시작점 추가

    while pq:
        weight, now = heappop(pq)
        if MST[now]:    # 이미 더 짧은 거리로 방문했다면 continue
            continue

        MST[now] = 1    # 방문 처리
        sum_weight += weight

        for to in range(V+1):
            if graph[now][to] == 0 or MST[to] == 1:
                continue
            heappush(pq, (graph[now][to], to))

    print(f'#{tc} {sum_weight}')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split()) # 출발, 도착, 가중치
        # 무방향 그래프
        graph[s][e] = w
        graph[e][s] = w

    prim(0)