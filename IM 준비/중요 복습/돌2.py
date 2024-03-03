"""
마주보는 j개의 돌에 대해 같은 색이면 뒤집고 다른 색이면 그대로
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):
            if 0 < i-k and i+k <= N and arr[i-k] == arr[i+k]:
                if arr[i-k] == 1:
                    arr[i-k] = 0
                    arr[i+k] = 0
                else:
                    arr[i-k] = 1
                    arr[i+k] = 1
    print(f'#{tc}', *arr[1:])