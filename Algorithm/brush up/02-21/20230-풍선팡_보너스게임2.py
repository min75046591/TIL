"""
N x N 맵
풍선을 터트리면 같은 행과 열의 풍선이 모두 터짐

최대 점수를 구하라
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for p in range(1, N+1):
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i+di*p, j+dj*p
                    if 0<=ni<N and 0<=nj<N:
                        s += arr[ni][nj]

            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')