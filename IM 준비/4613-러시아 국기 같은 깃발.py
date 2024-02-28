"""
W 흰색
B 파란색
R 빨간색

새로 칠해야 하는 칸의 개수의 최솟값을 구하라
"""

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 줄의 개수, M 한 줄당 문자의 개수
    arr = [list(input()) for _ in range(N)]
    # 그 라인에 다른 색깔이 있다면 x로 바꾸기
    # 마지막에 x의 개수를 세서 최소개수 구하기]
    
