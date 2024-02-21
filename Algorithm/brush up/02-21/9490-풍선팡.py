"""
터트린 풍선의 꽃가루 개수만큼 상하좌우 풍선이 추가로 1개씩 터짐
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for p in range(1, s + 1):  # for p in range(1, arr[i][j]+1)
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:

                    ni, nj = i+di*p, j+dj*p
                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]

            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')