def mins(i, j, s):
    global min_v

    if i >= N or j >= N:    # i, j가 범위를 벗어난 경우
        return

    elif i == N-1 and j == N-1:  # 도착했을 경우
        if min_v > s + arr[N-1][N-1]:
            min_v = s + arr[N-1][N-1]

    elif min_v <= s:
        return

    else:
        mins(i+1, j, s + arr[i][j])
        mins(i, j+1, s + arr[i][j])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 4000
    mins(0, 0, 0)
    print(f'#{tc} {min_v}')