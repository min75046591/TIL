def rotation(a, N):
    blank = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            blank[x][N - 1 - y] = a[y][x]

    return blank


T = int(input())
for tc in range(1, T + 1):
    square = int(input())
    lst = list((input().split()) for _ in range(square))

    rotation_90 = rotation(lst, square)
    rotation_180 = rotation(rotation_90, square)
    rotation_270 = rotation(rotation_180, square)

    print(f"#{tc}")
    for i, j, k in zip(rotation_90, rotation_180, rotation_270):
        print(f"{''.join(i)} {''.join(j)} {''.join(k)}")



