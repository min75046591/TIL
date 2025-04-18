tetro = [[(0,1), (0,2), (0,3)],
         [(1,0), (2,0), (3,0)],
         [(0,1), (1,0), (1,1)],
         [(-2,0), (-1,0), (0,1)],
         [(0,1), (0,2), (1,0)],
         [(0,-1), (1,0), (2,0)],
         [(0,-2), (0,-1),(-1,0)],
         [(0,-1), (-1,0), (-2,0)],
         [(-1,0), (0,1), (0,2)],
         [(0,1), (1,0), (2,0)],
         [(0,-2), (0,-1), (1,0)],
         [(-1,0), (0, 1), (1,1)],
         [(0,1), (1,0), (1,-1)],
         [(-1,0), (0,-1), (1,-1)],
         [(-1,-1), (-1,0), (0,1)],
         [(0,-1), (0,1), (1,0)],
         [(0,-1), (-1,0), (1,0)],
         [(0,-1), (-1,0), (0,1)],
         [(-1,0), (0,1), (1,0)]]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
minV = 0
for i in range(N):
    for j in range(M):
        for x in tetro:
            s = arr[i][j]
            for k in range(3):
                if 0<=i+x[k][0]<N and 0<=j+x[k][1]<M:
                    s += arr[i+x[k][0]][j+x[k][1]]
                else:
                    s = 0
                    break
            if minV<s:
                minV = s
print(minV)