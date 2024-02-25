#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_v = 1000000
    max_v = 0
    s = 0               # 구간의 합
    for i in range(M):  # 첫 구간의 합
        s += arr[i]

    min_v = max_v = s

    for i in range(N-M):    # 이미 계산된 구간의 합에서 제외할 맨 앞 원소
        s -= arr[i]
        s += arr[i+M]       # 현재 구간 다음 원소를 구간에 추가
        if min_v > s:
            min_v = s
        if max_v < s:
            max_v = s


'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    num_len = int(input())
    num_list = list(map(int, input().split()))
    max_val = num_list[0]
    min_val = num_list[0]

    for j in num_list:
        if j > max_val:
            max_val = j
        elif j < min_val:
            min_val = j
    result = max_val - min_val
    print(f'#{i} {result}')
'''