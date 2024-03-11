T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(i, i+j):
            if k < N+1 and k > 0:
                arr[k] = arr[i]

    print(f'#{tc}', *arr[1:] )