"""
정사각형 가로 세로가 10인
영역의 넓이를 구하라
"""

N = int(input())    # 색종이 개수
arr = [[0]*100 for _ in range(100)]
for n in range(N):
    j, i = map(int, input().split())

    for k in range(i, i+10):
        for l in range(j, j+10):
            arr[k][l] = 1

cnt = 0
for p in range(100):
    for q in range(100):
        if arr[p][q] == 1:
            cnt += 1
print(cnt)