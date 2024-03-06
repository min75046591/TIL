T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for k in range(r1, r2+1):
            for l in range(c1, c2+1):
                board[k][l] += color # 색별로 색칠하기

    cnt = 0
    for p in range(10):
        for q in range(10):
            if board[p][q] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')