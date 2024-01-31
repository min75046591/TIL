'''
빨강은 +1, 파랑은 +1, 겹치는 보라색은 3으로 나옴
겹치는 영역의 개수를 구하라
'''

# 입력
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    square = [[0]*10 for _ in range(10)]  # 10*10 행렬

    for area in range(N):
        r1, c1, r2, c2, color = (map(int, input().split()))
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                square[i][j] += color

    count = 0
    for i in range(10):
        for j in range(10):
            if square[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')