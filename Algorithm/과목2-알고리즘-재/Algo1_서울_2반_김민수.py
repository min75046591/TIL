"""
도화지에 도장을 찍어서 칠해진 칸이 모두 몇 칸인지
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 도화지의 크기, M 도장을 찍은 횟수
    bd = [[0]*N for _ in range(N)]      # 도화지 N*N 크기
    cnt = 0  # 도장 개수
    for _ in range(M):
        r1, c1, r2, c2 = map(int, input().split())  # 왼쪽 위 좌표와 너비와 높이

        for i in range(r1, r1+c2):          # 행부터 행의 길이만큼
            for j in range(c1, c1+r2):      # 열부터 열의 길이만큼
                if 0 <= i < N and 0 <= j < N:   # 도화지를 벗어나면 안됀다.
                    bd[i][j] = 1                # 도장 표시하기
    # 도화지를 탐색하며 도장으로 찍힌 부분 카운트
    for k in range(N):
        for l in range(N):
            if bd[k][l] == 1:   # 도장이 찍혀있으면
                cnt += 1        # 카운트 +1
    
    print(f'#{tc} {cnt}')