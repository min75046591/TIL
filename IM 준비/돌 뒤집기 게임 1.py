"""
i 번째부터 j개의 돌을 i번째 돌의 색으로 바꾸기

"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(j):
            if i+k <= N:
                arr[i+k] = arr[i]

    print(f'#{tc}', *arr[1::])