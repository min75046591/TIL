R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(R):
    if A[i][0]==-1:
        cleaner.append(i)
org = A
for _ in range(T):
    dest = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if org[i][j]>0: # 미세먼지가 있으면 확산
                diffuse = []
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0<=ni<R and 0<=nj<C and org[ni][nj]!=-1:
                        diffuse.append((ni, nj))
                v = org[i][j]//5
                for x in diffuse:
                    dest[x[0]][x[1]] += v
                dest[i][j] += org[i][j]-v*len(diffuse)
    # 공기순환
    for i in range(cleaner[0]-1, 0, -1): # 청정기 윗칸까지
        dest[i][0] = dest[i-1][0]
    for i in range(0, C-1):
        dest[0][i] = dest[0][i+1]
    for i in range(0, cleaner[0]):
        dest[i][C-1] = dest[i+1][C-1]
    for i in range(C-1, 0, -1):
        dest[cleaner[0]][i] = dest[cleaner[0]][i-1]

    for i in range(cleaner[1]+1, R-1):
        dest[i][0] = dest[i+1][0]
    for i in range(0, C-1):
        dest[R-1][i] = dest[R-1][i+1]
    for i in range(R-1, cleaner[1], -1):
        dest[i][C-1] = dest[i-1][C-1]
    for i in range(C-1, 0, -1):
        dest[cleaner[1]][i] = dest[cleaner[1]][i-1]

    org = dest
    org[cleaner[0]][0] = -1
    org[cleaner[1]][0] = -1

s = 0
for i in range(R):
    s += sum(org[i])
print(s+2) # 청정기부분 제외