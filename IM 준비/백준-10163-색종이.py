"""
N장의 색종이가 주어진 위치에 차례로 놓일 경우,
각 색종이가 보이는 부분의 면적을 구하라
색종이가 안보이면 0을 출력
"""
N = int(input())
arr = [[0] * 101 for _ in range(101)]

for num in range(1, N+1):
    j, i, c1, c2 = map(int, input().split())
    for k in range(i, i+c2):
        for l in range(j, j+c1):

            arr[k][l] = num


for v in range(1, N+1):
    cnt = 0
    for p in range(101):
        for q in range(101):
            if arr[p][q] == v:
                cnt += 1
    print(cnt)
