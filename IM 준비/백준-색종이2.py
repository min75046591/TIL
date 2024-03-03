"""
길이가 각각 10인 정사각형
색종이가 붙은 검은 영역의 둘레의 길이를 구하라
"""
N = int(input())
arr = [[0]*101 for _ in range(101)]
cnt = 0
for k in range(N):
    j, i = map(int, input().split())

    for p in range(i, i+10):
        for q in range(j, j+10):
            arr[p][q] += 1

for x in range(101):
    for y in range(101):
        if arr[x][y] >= 1:
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = x + di, y + dj
                if 0 <= ni < 101 and 0 <= nj < 101 and arr[ni][nj] == 0:
                    cnt += 1

                # elif ni < 0 or ni >= 101 or nj < 0 or ni >= 101:
                #     cnt += 1
print(cnt)