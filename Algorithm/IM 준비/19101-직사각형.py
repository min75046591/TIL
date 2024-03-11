"""
직사각형 1
선분 2
점 3
공통 부분이 없음 4

첫 네개의 정수는 첫 번째 직사각형. 나머지 4개의 정수형은 두 번째 직사각형
"""
T = int(input())
for tc in range(1, T+1):
    arr = [[0]*1001 for _ in range(1001)]
    x1, y1, p1, q1 = map(int, input().split())
    x2, y2, p2, q2 = map(int, input().split())
    result = 0

    # 첫 번째 직사각형
    for i in range(x1, p1+1):
        for j in range(y1, q1+1):
            arr[i][j] += 1


    # 두 번째 직사각형형
    for k in range(x2, p2+1):
        for l in range(y2, q2+1):
            arr[k][l] += 1


    # 맵 탐색 하며 조건 탐색
    w = 0
    h = 0
    for row in arr:
        if 2 in row:
            h += 1
            w = row.count(2)
    # 꼭지점에서 만날 때
    if w == 1 and h == 1:
        result = 3
    # 선분으로 만날 때
    elif (w == 1 and h > 1) or (h == 1 and w > 1):
        result = 2
    # 직사각형으로 만날 때
    elif w > 1 and h > 1:
        result = 1
    else:
        result = 4

    print(f'#{tc} {result}')