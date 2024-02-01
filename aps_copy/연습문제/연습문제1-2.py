# 입력 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

for i in range(N):  # 25개의 각 요소에 대해서 arr[i][i]
    for j in range(N):
        for di, dj in [[0,1],[1,0],[0,-1][-1,0]]:   # 그 요소와 이웃(상하좌우)한 요소 arr[ni][nj]
            ni, nj = 1+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                total += abs(arr[ni][nj]-arr[i][j]) # 차의 절대값을 구하시오, 총합을 구하시오.

print(total)


# 2번째 풀이
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

for i in range(N):  # 25개의 각 요소에 대해서 arr[i][i]
    for j in range(N):
        for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            total += abs(arr[ni][nj] - arr[i][j]) # 차의 절대값을 구하시오, 총합을 구하시오.

print(total)