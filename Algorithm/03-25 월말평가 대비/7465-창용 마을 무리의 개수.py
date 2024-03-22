"""
N명의 사람. 두 사람은 서로를 알고 있는 관계 or 모르는 관계
두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
이러한 사람들을 모두 다 묶어서 하나의 무리

창용 마을에 몇 개의 무리가 존재하는지 계산
"""
import sys
sys.stdin = open("input.txt", "r")

def bfs(s):
    q = [s]
    visited[s] = 1

    while q:
        now = q.pop(0)
        for next in graph[now]:
            if visited[next]:   # 이미 방문 한 곳은 pass
                continue
            q.append(next)          # 다음에 갈 노드 큐에 push
            visited[next] = 1  # 방문 표시

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0         # 무리 수

    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e) # 양방향 그래프
        graph[e].append(s)

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')