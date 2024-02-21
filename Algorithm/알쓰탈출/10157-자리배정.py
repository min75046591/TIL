"""
가로는 C, 세로는 R
가장 왼쪽 아래부터 (1,1)
가장 오른쪽 위 좌석은 (7,6)

달팽이 문제와 비슷

대기번호 K인 관객에게 배정될 좌석번호 (x,y)를 구해 x, y를 공백을 사이에 두고 출력
"""

# 실패..ㅠ
# https://jennnn.tistory.com/3
# https://velog.io/@hovelopin/%EC%BD%94%ED%85%8C-%EB%8B%AC%ED%8C%BD%EC%9D%B4-%EB%B0%B0%EC%97%B4
C ,R = map(int, input().split())    # C 가로, R 세로
K = int(input())                    # 대기번호
seat_map = [[0]*C for _ in range(R)]
result = []
# 위 오른 아래 왼
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dir = 0
i = j = 0
seat_map[i][j] = 1        # 시작 지점에 1 표시
K = K - 1            # 첫 번째 사람을 시작지점에 배정
while K <= 0:
    ni, nj = i+di[dir], j+dj[dir]
    if 0 <= ni < R and 0 <= nj < C and seat_map[ni][nj] == 0:
        seat_map[ni][nj] = 1
        K -= 1
        i, j = ni, nj
        if K == 0:
            result.append((ni+1, nj+1))
    else:
        dir = (dir+1)%4
print(result, end='')