# 입력값 받기
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split()))  # 양수 입력값
    
    min_idx = 0  # 맨 앞을 최소값 위치로 가정
    max_idx = 0  # 맨 앞을 최대값 위치로 가정

    for i in range(N):
        # 가장 작은 수가 여러 개이면 먼저 나오는 위치 >
        if arr[min_idx] > arr[i]:   # 지금까지의 최솟값보다 arr[i]가 더 작으면
            min_idx = i
        # 가장 큰 수가 여러 개이면 마지막으로 나오는 위치 <=
        if arr[max_idx] <= arr[i]:
            max_idx = i

    ans = max_idx - min_idx if max_idx>min_idx else min_idx-max_idx
    print(f'#{tc} {ans}')