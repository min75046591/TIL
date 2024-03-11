"""
각 카드는 양의 정수
딜러가 N장의 카드를 숫자가 보이도록 내려놓음 그런 후에 숫자 M을 외침

플레이어는 제한된 시간에 N장의 카드 중 3장의 카드를 골라야함
플레이어가 고른 카드의 합이 M을 넘지 않고 M과 최대한 가깝게 만들어야 함

M을 넘지 않으면서 M과 최대한 가깝게 만든 3장의 카드 합을 출력!
"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = arr[i] + arr[j] + arr[k]
            if max_v < sum_v and sum_v <= M:
                max_v = sum_v

print(max_v)