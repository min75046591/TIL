C, R = map(int, input().split())    # 가로로 C, 세로로 R
K = int(input())                # 대기번호

if R*C < K:         # 배정이 불가능한 경우 0
    print(0)
else:               # 배정하면서 K가 되면 그때 좌표 출력
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    # 주변을 1로 둘러싸면: 범위체크 필요 없음
    arr = [[1]*(C+2)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1]*(C+2)]

    i, j, dr = 1, 1, 0
    for n in range(1, K):
        arr[i][j] = n
        ni, nj = i+di[dr], j+dj[dr]
        if arr[ni][nj] == 0:        # 비어있으니 이동 가능
            i, j = ni, nj
        else:
            dr = (dr+1)%4     # 범위 밖 또는 이미 기록한 위치 -> 방향을 꺾어서 진행
            i, j = i+di[dr], j+dj[dr]

    print(f'{j} {i}')
