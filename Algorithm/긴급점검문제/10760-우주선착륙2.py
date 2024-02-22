"""
착륙지점을 중심으로 주변 8개 구역중 착륙 지점보다 높이가 낮은
구역의 사진을 찍을 수 있다.
극한상황을 대비해 예비후보지를 선정
예비후보지는 8개의 방향중 사진을 찍을 수 있는 방향이 4방향 이상인 지점
예비후보지의 수를 알아내라

주변에 높이 정보가 없는 영역이 있어도 알려진 영역의 높이만 조건을
만족하면 후보지에 포함

파리문제 비슷
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 맵 탐색
    for i in range(N):
        for j in range(M):
            # 착륙지를 기준으로 8방향 조사
            cnt = 0     # 주변에 나보다 낮은 높이 개수
            tall = arr[i][j]    # 착류지점 높이

            # 주변 8방향 탐색
            for di, dj in [[0,1], [1,0], [-1,0], [0,-1], [1,-1], [-1,1], [1,1], [-1,-1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] < tall:
                    cnt += 1
            if cnt >= 4:        # 낮은지점 4 이상시 결과에 +1
                result += 1
    print(f'#{tc} {result}')