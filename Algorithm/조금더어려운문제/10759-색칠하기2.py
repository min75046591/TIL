"""
색칠하고 겹친 부분을 제외한 빨간색과 파란색의 영역의 길이를 구하라
결과값 = 빨간색 길이  + 파란색 길이
빨강 = 1
파랑 = 2
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 칠할 영역의 개수
    paper = [[0]*10 for _ in range(10)]     # 맵 만들기
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

    # 색칠하기
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                paper[i][j] += color
                # 빨강 파랑 중 상하좌우 확인해서 자기 값과 다르면 cnt + 1

                if paper[i][j] == 3:
                    paper[i][j] = 0

    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 or paper[i][j] == 2:
                for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < 10 and 0 <= nj < 10 and paper[ni][nj] != paper[i][j]:
                        cnt += 1
                    elif ni < 0 or ni >= 10 or nj < 0 or nj >= 10:           # 가장자리면 길이 추가
                        cnt += 1

    print(f'#{tc} {cnt}')