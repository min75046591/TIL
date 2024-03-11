T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt_1 = 1  # 가로
    cnt_2 = 1  # 세로

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                for di, dj in [[1,0], [0,1]]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '.':
                        if arr[ni][nj] == '#':
                            arr[i][j] = arr[ni][nj]
                            cnt_1 += 1
                            cnt_2 += 1



    if cnt_1 == cnt_2 and cnt_1 > 1 and cnt_2 > 1:
        result = 'yes'
    else:
        result = 'no'

    print(f'#{tc} {result}')