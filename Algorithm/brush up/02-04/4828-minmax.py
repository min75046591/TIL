T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = map(int, input().split())

    max_v = 0
    min_v = 999999
    for i in arr:
        if max_v < i:
            max_v = i

        if min_v > i:
            min_v = i

    result = max_v - min_v
    print(f'#{tc} {result}')