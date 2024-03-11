T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                # 위 오른쪽위 오른쪽 오른쪽아래
                for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1]]:
                    cnt = 1
                    ni, nj = i+di, j+dj
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni, nj = ni + di, nj + dj
                        if cnt == 5:
                            result = 'YES'
                            break


    print(f'#{tc} {result}')