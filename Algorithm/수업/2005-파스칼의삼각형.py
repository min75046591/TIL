T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:  # 첫줄과 대각선을 1로 채움
                arr[i][j] = 1
            # 그 외의 공간. 즉 (-1, -1)과 (-1, 0)위치를 더해서 나온 값.
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    
    print(f'#{tc}')
    for k in range(N):
        for l in range(k+1):
            print(arr[k][l], end = ' ')
        print()