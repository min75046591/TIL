"""
N * M 크기의 격자판
풍선이 터지면 상하좌우의 풍선이 추가로 터짐

A 풍선에 들어있는 꽃가루 개수
꽃가루 수 중 최대값을 출력
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 세로, M 가로
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    # 상 하 좌 우
    # di = [-1, 1, 0, 0]
    # dj = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            cnt = 0
            cnt += arr[i][j]    # 현재 내가 위치한 좌표의 꽃가루 더하기
            # 상하좌우 꽃가루 카운트
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M:
                    cnt += arr[ni][nj]

                if max_cnt < cnt:
                    max_cnt = cnt

    print(f'#{tc} {max_cnt}')