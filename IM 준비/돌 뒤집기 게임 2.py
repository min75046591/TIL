"""
i 번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 같은 색이면 뒤집고 다른 색이면 그대로 둔다
돌을 벗어나는 경우 뒤집기는 중지
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for p in range(1, j+1):
            if 0<i-p and i+p<=N and arr[i-p] == arr[i+p]:
                if arr[i-p] == 1:
                    arr[i-p] = 0
                    arr[i+p] = 0
                else:
                    arr[i-p] = 1
                    arr[i+p] = 1

    print(f'#{tc}', *arr[1:])


