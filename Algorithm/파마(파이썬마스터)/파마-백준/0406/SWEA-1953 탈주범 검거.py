"""
탈주범은 시간당 1의 거리를 움직일 수 있음
중복 가능 -> 지나간 장소 다시 갈 수 있음
"""
from collections import deque

def catch(r, c):
    s = deque((r, c))    # 시작 위치 인큐
    if







T = int(input())
for tc in range(1, T+1):
    # 터널 지도의 세로 N, 가로 M, 맨홀 뚜껑이 위치한 장소의 세로 R, 가로 C, 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    cage = [list(map(int, input().split())) for _ in range(N)]
    start = (R, C)
    catch(R, C)  # 시작 위치

    # 방문 위치 찾기
    for i in range(N):
        for j in range(M):
            if cage[i][j] ==