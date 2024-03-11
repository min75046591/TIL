"""
L 미터의 롤 케이크
방청객 N명에게 케이크를 나누어 줌
가장 왼쪽 조각이 1번, 오른쪽 조각이 L번

방청객은 1번부터 N번까지 번호
각 방청객은 자신이 원하는 조각을 적어서 냄
이 떄 두 수 P와 K를 내며, P부터 K번까지 원한다는 말임

1번 방청객의 종이부터 순서대로 펼쳐서 해당하는 조각에 그 사람의 번호를 적어서 냄
이미 적혀있는 조각은 번호를 적지 못함

가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호 -> 가장 넗은 범위. 즉 P-K가 가장 큰 사람
실제로 가장 많은 케이크 조각을 받는 방청객의 번호
위의 두 가지를 구하라!
"""
L = int(input())    # 케이크 길이
N = int(input())    # 방청객 수
arr = [0] * (L+1)     # 케이크
max_N = 0   # 가장 많은 케이크 조각을 받을 것을로 기대한 방청객의 번호
v = 0       # 가장 큰 P-K값
real_N = 0  # 실제로 많이 받은 방청객 번호
max_cnt = 0  # arr 에 가장 많이 들어있는 방청객 번호

for nums in range(1, N+1):  # 두개의 번호 P, K
    P, K = map(int, input().split())
    # 기대한 방청객 번호
    max_pk = K-P
    if v < max_pk:
        v = max_pk
        max_N = nums

    # 롤케이크에 방청객 번호 넣기
    for i in range(P, K+1):
        if arr[i] > 0:
            continue
        elif arr[i] == 0:
            arr[i] = nums

    cnt = 0
    for g in range(1, L+1):
        if arr[g] == nums:
           cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        real_N = nums

print(max_N)
print(real_N)