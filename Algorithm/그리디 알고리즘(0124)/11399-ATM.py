'''
N = 줄을 선 사람 수
사람은 1번부터 N번까지 번호
i번 사람이 돈을 인출하는데 걸리는 시간 = Pi분

줄을 서는 순서에 따라 시간의 합이 달라짐

-> 각 사람이 돈을 인출하는데 필요한 시간의 최소 합

'''

N = int(input())
pi = map(int, input().split())

sort_list = sorted(pi)
result = 0

for i in range(N):
    if i >= 1:
        sort_list[i] += sort_list[i-1]

for i in sort_list:
    result += i
print(result)
