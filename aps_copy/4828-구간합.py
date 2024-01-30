#import sys
#sys.stdin = open("input.txt", "r")

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