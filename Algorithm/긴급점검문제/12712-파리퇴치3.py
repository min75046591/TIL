"""
N*N

스프레이가 + 아니면 x 중 하나로 분사
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # M은 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    max_s = 0
    for i in range(N):
        for j in range(N):
            s1 = arr[i][j]
            s2 = arr[i][j]

            for p in range(1, M):
                # + 자 -> 상 하 좌 우
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i + di * p, j + dj * p
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]

                # x 자 -> 오위 오아래 왼위 왼아래
                for xi, xj in [[-1, 1], [1, 1], [-1, -1], [1, -1]]:
                    xi, xj = i + xi * p, j + xj * p
                    if 0 <= xi < N and 0 <= xj < N:
                        s2 += arr[xi][xj]

                if s1 < s2:
                    max_s = s2
                elif s1 > s2:
                    max_s = s1
            if max_v < max_s:
                max_v = max_s

    print(f'#{tc} {max_v}')


# 버전 2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # M은 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            s1 = arr[i][j]
            s2 = arr[i][j]

            for p in range(1, M):
                # + 자 -> 상 하 좌 우
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i + di * p, j + dj * p
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]

                # x 자 -> 오위 오아래 왼위 왼아래
                for xi, xj in [[-1, 1], [1, 1], [-1, -1], [1, -1]]:
                    xi, xj = i + xi * p, j + xj * p
                    if 0 <= xi < N and 0 <= xj < N:
                        s2 += arr[xi][xj]

            if max_v < s1:
                max_v = s1
            if max_v < s2:
                max_v = s2

    print(f'#{tc} {max_v}')