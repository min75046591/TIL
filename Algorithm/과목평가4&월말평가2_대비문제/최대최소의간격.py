"""
최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력
가장 작은 수가 여러 개이면 먼저 나오는 위치
가장 큰 수가 여러 개이면 마지막으로 나오는 위치
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_v = 11
    max_v = 0
    k = l = 0
    for i in range(N):
        if min_v > arr[i]:
            min_v = arr[i]
            k = i
    for j in range(N):
        if max_v <= arr[j]:
            max_v = arr[j]
            l = j
    result = abs(l-k)
    print(f'#{tc} {result}')