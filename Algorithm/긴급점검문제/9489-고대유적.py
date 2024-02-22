"""
구조물은 폭 1m, 길이 2m 이상의 직선
서로 평행 or 직각으로만 자리
구조물이 있는 자리는 1로 나타냄

맵은 N x M

겹친건 서로 다른 깊이에 묻힌 것이므로 직선만 고려하면 됌
구조물은 서로 1m 이상 떨어져있고 구조물의 최소 크기는 1x2m
N 개의 줄에 M개씩 데이터

가장 긴 구조물의 길이를 구하라!
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        cnt = 0             # 행을 바꿨을때 초기화
        for j in range(M):
            if arr[i][j] == 1:
                for di, dj in [[1, 0], [0, 1]]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                        cnt += 1



                # 최대 길이
                if max_cnt < cnt:
                    max_cnt = cnt

    print(f'#{tc} {max_cnt}')


