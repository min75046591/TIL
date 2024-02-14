"""
100 x 100 도화지
가로세로 10인 검은색 색종이
색종이가 붙은 검은 영역의 넓이를 구하라
"""

N = int(input()) # 색종이 수
M = [[0]*100 for _ in range(100)] # 도화지
for _ in range(N):    
    i, j = map(int, input().split())  # 색종이와 도화지의 왼쪽 변, 아래쪽 변 사이의 거리
    for k in range(i, i+10): # 색종이 위치에 
        for l in range(j, j+10):
            M[k][l] = 1      # 1을 넣기
    
cnt = 0
for x in range(100):
    for y in range(100):
        if M[x][y] == 1:
            cnt += 1
print(cnt)