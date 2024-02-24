T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    first = 0
    a = b = c = d = 0
    cnt = 0             # 멧돼지 수
# 왼쪽 위 모서리
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and first == 0:
                first += 1
                a, b = i, j

# 오른쪽 아래 모서리
    for k in range(N-1, -1, -1):
        for l in range(N-1, -1, -1):
            if arr[k][l] == 1 and first == 1:
                first += 1
                c, d = k, l

# 감시카메라 범위 안의 멧돼지 수 구하기
    for p in range(a+1):
        for q in range(b+1):
            if arr[p][q] == 2:
                cnt += 1

    for p in range(c, N):
        for q in range(d, N):
            if arr[p][q] == 2:
                cnt += 1

    for p in range(c, N):
        for q in range(b+1):
            if arr[p][q] == 2:
                cnt += 1

    for p in range(a+1):
        for q in range(d, N):
            if arr[p][q] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')