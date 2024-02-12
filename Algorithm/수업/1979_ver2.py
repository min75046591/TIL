T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N:한 변의 길이  K:길이
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]+[[0]*(N+1)]
    # 끝에 0을 하나씩 추가한 것
    N += 1
    # 가로, 세로로 연속한 1의 개수가 K인 경우의 수
    ans = 0
    for i in range(N):  # i행에서 연속한 1의 개수
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:       # arr[i][j]==0 이면
                if cnt==K:
                    ans += 1
                cnt = 0

    for j in range(N):  # j열에서 연속한 1의 개수
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else:       # arr[i][j]==0 이면
                if cnt==K:
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans}')