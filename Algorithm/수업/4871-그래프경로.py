'''
V = 노드 개수
E = 노드 몇줄인지

S = 출발 노드
G = 도착 노드
'''
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [map(int, input().split()) for _ in range(E)]
    S, G = map(int, input().split())



