gear = [list(input()) for _ in range(4)]
top = [0]*4 # 12시 방향 인덱스
K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())

    tmp = top[num-1]
    turn = dir

    for i in range(num, 4): # 회전 톱니 오른쪽
        if gear[i-1][(tmp+2)%8] == gear[i][(top[i]+8-2)%8]: # 맞닿은 톱니가 같은 극이면 정지
            break
        else:
            turn *= -1
            tmp = top[i]
            if turn != 1:  # 반시계 방향
                top[i] = (top[i] + 1) % 8
            else:
                top[i] = (top[i] + 8 - 1) % 8
    tmp = top[num-1]
    turn = dir
    for i in range(num-2, -1, -1): # 회전 톱니 왼쪽
        if gear[i][(top[i]+2)%8] == gear[i+1][(tmp+8-2)%8]: # 맞닿은 톱니가 같은 극이면 정지
            break
        else:
            turn *= -1
            tmp = top[i]
            if turn != 1:  # 반시계 방향
                top[i] = (top[i] + 1) % 8
            else:
                top[i] = (top[i] + 8 - 1) % 8
    if dir!=1: #반시계 방향
        top[num-1] = (top[num-1]+1)%8
    else:
        top[num-1] = (top[num-1]+8-1)%8
score = 0
for i in range(4):
        score += int(gear[i][top[i]])* 2**i
print(score)
