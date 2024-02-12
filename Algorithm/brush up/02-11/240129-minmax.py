T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = map(int, input().split())
    max_num = 0
    min_num = 1000000
    for i in nums:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    result = max_num - min_num

    
    print(f'#{tc} {result}')