T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'yes'
    stop = False

    for y in range(N):
        for x in range(N):
            if stop == False:
                if arr[y][x] == '#':
                    start = x, y
                    cnt = 1

                    for k in range(1, N):
                        xx, yy = x+k, y+k
                        if 0 <= xx < N and 0 <= yy < N and arr[yy][xx] == '#':
                            cnt += 1
                            stop = True

    x, y = start
    for p in range(y, y+cnt):
        for q in range(x, x+cnt):
            if arr[p][q] == '#':
                arr[p][q] = '.'
            elif arr[p][q] == '.':
                ans = 'no'

    for b in arr:
        if '#' in b:
            ans = 'no'
            break

    print(f'#{tc} {ans}')