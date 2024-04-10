# 완탐
score = [0, 1, 10, 100, 1000]

N = int(input())
arr = [[0]*N for _ in range(N)]
student = [list(map(int, input().split())) for _ in range(N*N)]
#arr[1][1] = student[0][0]
for a,b,c,d,e in student:
    max_like = -1
    max_like_i = max_like_j = -1
    max_empty = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like = 0
                empty = 0
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 0:
                            empty += 1
                        elif arr[ni][nj] in [b,c,d,e]:
                            like += 1
                if max_like < like:
                    max_empty = empty
                    max_like = like
                    max_like_i = i
                    max_like_j = j
                elif max_like == like and max_empty < empty:
                    max_empty = empty
                    max_like_i = i
                    max_like_j = j
    arr[max_like_i][max_like_j] = a
total = 0
student.sort()
for i in range(N):
    for j in range(N):
        cnt = 0
        num, *tmp = student[arr[i][j]-1]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] in tmp:
                cnt += 1
        total += score[cnt]
print(total)