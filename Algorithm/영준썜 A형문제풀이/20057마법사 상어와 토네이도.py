'''
제출된 다른 사람 코드...

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mul = [2, 10, 7, 1, 5, 10, 7, 1, 2, 0]   # 비율 -> 나중에 100으로 나눠줌

ai = [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0],
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]]

aj = [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]]

#좌, 하, 우, 상
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

cnt_mx = 1
ci = cj = N//2
ans = dr = cnt = flag = 0
while (ci, cj)!=(0, 0):
    ci, cj = ci + di[dr], cj + dj[dr]

    #[1] ci, cj 기준좌표 중심으로 모래양 계산해서 추가, 범위밖=>ans추가
    if arr[ci][cj]>0:
        val = arr[ci][cj]   #기준 좌표 모래양
        arr[ci][cj] = sm = 0     # 기준 좌표 모래는 날라가서 없어짐

        for i in range(10): #0~9까지 위치 처리
            ni, nj = ci+ai[dr][i], cj+aj[dr][i]
            t=(val*mul[i])//100 #소수점 이하 버림

            if i == 9: #나머지 모래양 계산
                t=val-sm

            if 0<=ni<N and 0<=nj<N: #범위내라면
                arr[ni][nj]+=t
            else:
                ans+=t    #밖으로 나간 모래양의 추가
            sm+=t

    cnt+=1
    if cnt==cnt_mx:
        cnt=0
        dr = (dr+1)%4
        if flag==0:
            flag=1
        else:
            flag = 0
            cnt_mx+=1
print(ans)
'''



def f(i, j, amount, dir, N): # x(i,j), amount 모래양, dir:x->y 방향, N크기
    out = 0
    scatter = 0
    for a,b,c in tonado: # a 진행방향 거리, b좌우 거리, c 날리는 비율
        for LR in [(dir - 1) % 4, (dir + 1) % 4]: # 진향 방향 좌우
            ni, nj = i+di[dir]*a + di[LR]*b, j+dj[dir]*a+dj[LR]*b
            if 0<=ni<N and 0<=nj<N:
                arr[ni][nj] += int(amount*c) # 주변으로 날린 모래양, 소숫점 아래 버림
            else:
                out += int(amount*c)
            scatter += int(amount * c)
    ni, nj = i + di[dir] * 3, j + dj[dir] * 3  # 알파 다음
    if 0 <= ni < N and 0 <= nj < N:
        arr[ni][nj] += int(amount*0.05)
    else:
        out += int(amount*0.05)
    scatter += int(amount * 0.05)
    ni, nj = i+di[dir]*2, j+dj[dir]*2  # 알파
    if 0<=ni<N and 0<=nj<N:
        arr[ni][nj] += amount-scatter
    else:
        out += amount-scatter
    return out

# [x기준 진행칸, 좌우칸 거리, 모래비율]
tonado = [[0, 1, 0.01], [1,1,0.07],[1,2,0.02],[2,1,0.1]]

di = [ 0, 1, 0,-1]  # 오른쪽 부터 시계방향
dj = [1, 0, -1, 0]
# 모래 날리기, 진행방향의 오른쪽 (dir+1)%4, 왼쪽(dir+4-1)%4
# a y<-x


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#중심에서 출발
xi = xj = N//2
move = 1
dir = 2
k = 1
ans = 0
while True:
    for _ in range(move):
        k += 1
        yi, yj = xi+di[dir], xj+dj[dir]
        if arr[yi][yj]>0:
            ans += f(xi, xj, arr[yi][yj], dir, N)
            arr[yi][yj] = 0
        xi, xj = yi, yj
    dir = (dir-1)%4
    if k>N*N:
        break
    for _ in range(move):
        k += 1
        yi, yj = xi + di[dir], xj + dj[dir]
        if arr[yi][yj]>0:
            ans += f(xi, xj, arr[yi][yj], dir, N)
            arr[yi][yj] = 0
        xi, xj = yi, yj
    dir = (dir - 1) % 4
    move += 1
print(ans)


