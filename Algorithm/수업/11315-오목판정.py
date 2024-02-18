"""
N * N 판
가로, 세로, 대각선 중 하나의 방향으로 5개 이상 연속한 부분을 판정
'o' 돌이 있는 칸
'.' 돌이 없는 칸
연속한 부분이 있으면 YEs
없으면 NO
"""
def omok(N):
    for i in range(N):
        for j in range(N):
            # (i,j)에 돌이 있다면
            if map[i][j] == 'o':
                # 오른쪽, 오른쪽 위, 오른쪽 아래, 아래 방향
                for di, dj in [[0,1], [-1,1], [1,1], [1,0]]:
                    cnt = 1
                    ni, nj = i+di, j+dj  # 옮겨간 위치부터 조사 시작
                    while 0 <= ni < N and 0 <= nj < N and map[ni][nj] == 'o':
                        cnt += 1
                        if cnt == 5:
                            return 'YES'
                        ni, nj = ni+di, nj+dj  # 다음 위치를 방향으로 설정한 곳으로 이동
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map = [input() for _ in range(N)]
    print(f'#{tc} {omok(N)}')

