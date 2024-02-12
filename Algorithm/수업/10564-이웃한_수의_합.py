T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0] + arr[1]
    min_v = arr[0] + arr[1]

    for i in range(0, N-1):
        tmp_sum = arr[i] + arr[i+1]
        if max_v < tmp_sum:
            max_v = tmp_sum
        if min_v > tmp_sum:
            min_v = tmp_sum
    print(f'#{tc} {max_v} {min_v}')