T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]

    N += 1
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
        else:
            if cnt == K:
                ans += 1
            cnt = 0

    for j in range(N):
        if arr[i][j]:
            cnt += 1
        else:
            if cnt == K:
                ans += 1
                cnt = 0
