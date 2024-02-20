"""
직사각형들이 차지하는 면적을 구하라

직사각형에 해당하는 좌표에 1을 삽입
"""
arr = [[0]*100 for _ in range(100)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
# 직사각형 1로 채우기
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[y][x] = 1

# 직사각형이 차지하는 면적
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1
print(count)