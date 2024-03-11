T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                # 오 오른쪽아래 아래 왼쪽 아래
                for di, dj in [[0,1], [1,1], [1,0], [1, -1]]:
                    cnt = 1
                    ni, nj = i+di, j+dj
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                        cnt += 1
                        if cnt == 5:
                            result = 'YES'
                            break
                        ni, nj = ni + di, nj + dj   # 5가 될 때 까지 이동

    print(f'#{tc} {result}')

# ver.2
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_array = [input() for _ in range(N)]

    result = 'NO'
    for i in range(N):  # arr 돌면서,
        for j in range(N):
            if N_array[i][j] == 'o':  # 만약 "o"이 있다면, count = 1을 해주고,
                # 돌이 있는 지 확인
                for di, dj in [[0, 1], [1, 0], [1, 1], [1, -1]]:  # 상하좌우로 "o"이 있는지 탐색
                    cnt = 1
                    for k in range(1, 5):
                        ni = i + di * k # 현재위치 i에서 --> next i
                        nj = j + dj * k  # 현재위치 j에서 --> next j
                        if 0 <= ni < N and 0 <= nj < N and N_array[ni][nj] == 'o':
                            cnt += 1

                            if cnt == 5:
                                result = 'YES'
                                break
    print(f'#{tc} {result}')
