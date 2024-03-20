"""
N * N 도시    빈 칸(0), 치킨집(2), 집(1) 중 하나이다.
r행 c열. r과 c는 1부터 시작

치킨거리 : 집과 '가장' 가까운 치킨집 사이의 거리.
치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 갖고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합

두 칸 사이의 거리는 abs(r1 - r2) + abs(c1 - c2)

수익 증가를 위해 일부 치킨집을 폐업.
가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 폐업시켜야 함.
어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하라!
"""
def dfs(r):
    if r==M:





N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]




from itertools import combinations

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i + 1, j + 1))
        elif graph[i][j] == 2:
            chicken.append((i + 1, j + 1))

result = n * 2 * len(house)
for comb in list(combinations(chicken, m)):
    dist = 0
    for a, b in house:
        temp = n * 2
        for x, y in comb:
            temp = min(temp, abs(a - x) + abs(b - y))
        dist += temp
    result = min(result, dist)

print(result)