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

def sh_time():
    result = 0
    for i in range(N):
        i[i] += i[i+1]
        result += i[i]

        print(result)