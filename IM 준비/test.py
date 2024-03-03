T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_array = [input() for _ in range(N)]

    result = 'NO'
    for i in range(N):  # arr 돌면서,
        for j in range(N):
            if N_array[i][j] == 'o':  # 만약 "o"이 있다면, count = 1을 해주고,
                # 돌이 있는 지 확인
                for k in range(1, 5):
                    # 오른쪽 아래 오른쪽아래 왼쪽 아래로 "o"이 있는지 탐색
                    for di, dj in [[0, 1], [1, 0], [1, 1], [1, -1]]:
                        ni = i + di * k # 현재위치 i에서 --> next i
                        nj = j + dj * k  # 현재위치 j에서 --> next j
                        if 0 <= ni < N and 0 <= nj < N and N_array[ni][nj] == 'o':
                            cnt += 1

                            if cnt == 5:
                                result = 'YES'
                                break
    print(f'#{tc} {result}')