"""
오늘부터 N+1일째 되는 날 퇴사를 하기위해
남은 N일 동안 최대한 많은 상담

하루에 하나씩 서로 다른 사람의 상담

각각의 상담을 완료하는데 걸리는 기간 T와 상담을 했을 때 받을 수 있는 금액 P
"""
N = int(input())
arr = [0] + [list(map(int, input().split())) for _ in range(N)]
# print(day[1])
max_v = 0       # 최대 이익
for i in range(1, N+1):     # 1일부터 N일까지
    money = 0               # 각 상담을 진행했을때 최종적으로 번 돈
    if arr[i][0] <= N-i:    # N일중 arr[i][0]에 해당하는 날이 남아있는 날보다 작을 때만 가능
        money += arr[i][1]  # 상담 시작점 더하기
        for 



