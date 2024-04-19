"""
N * N 배열
1개의 셀에는 1개의 코어 아니면 전선이 올 수 있음
가장자리에는 전원이 흐르고 있음
코어와 전원을 연결하는 전선은 직선으로만 설치 가능
전선은 절대로 교차하면 안됌
가장자리에 위치한 코어는 이미 전원이 연결된 것으로 간주

최대한 많은 코어에 전원을 연결해도, 전원이 연결되지 않는 코어가 존재할 수 있음

최대한 많은 코어에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 함
여러 방법들 중 전선 길이의 합이 최소가 되는 값을 구하라!

0은 빈 셀 / 1은 코어
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Macintosh = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Macintosh[i][j] == 1:
                for di, dj in ([-1, 0], [1, 0], [0, 1], [0, -1]):
                    ni, nj = i+di, j+dj
                    if ni 