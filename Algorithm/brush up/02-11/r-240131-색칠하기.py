T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map = [[0]*10 for _ in range(10)]
    # 색칠하기
    for area in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                map[i][j] += color
    # 겹친 곳 세기
    count = 0
    for i in range(10):
        for j in range(10):
            if map[i][j] == 3:
                count += 1
    print(f'#{tc} {count}')