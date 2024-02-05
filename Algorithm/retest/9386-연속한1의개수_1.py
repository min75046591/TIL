T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 수열의 길이
    arr = list(map(int, input()))
    cnt = 0
    max_v = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            if max_v < cnt:
                max_v = cnt
        else:
            cnt = 0
    print(f'#{tc} {max_v}')