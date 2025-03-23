# 백준 - 1916

"""
N개의 도시
한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스
A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하라!

첫 째줄 도시의 개수 N
둘 째줄 버스의 개수 M

셋 째줄 부터 M+2줄 까지 버스의 정보
<버스의 출발 도시의 번호>, <도착지의 도시 번호>, <버스 비용>
버스 이용 : 0 <= cost < 100,000

마지막 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어짐.
단, 출발점에서 도착점으로 갈 수 있는 경우만 입력으로 주어짐
"""
# 그리디 문제?!

# (도착 - 출발) 의 값이 크고 비용은 적으면 좋다
# 비용순으로 정렬하고, 적은 비용이면서 (도착 - 출발)의 값이 큰걸 우선 뽑자

N = int(input())    # 도시의 수
M = int(input())    # 버스의 수
buses = []
for _ in range(M):
    bus = list(map(int, input().split()))
    buses.append(bus)
course = list(map(int, input().split()))

def sort_buses(buses):
    # sorted_buses = sorted(buses, key=operator.itemgetter(0))    # 출발 도시를 기준으로 정렬 / import operator를 사용했을 때 가능
    sorted_buses = sorted(buses, key=lambda x: (x[0]))     # 비용을 기준으로 정렬
    return sorted_buses

finish_sorted_buses = sort_buses(buses)
for bus in finish_sorted_buses:
    print(bus)

# 그리디가 아닌  문제!!!

