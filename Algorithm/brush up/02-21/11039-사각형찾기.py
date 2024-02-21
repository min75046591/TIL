"""
N x N 맵
0으로 채워진 맵에서 1로 표시된 영역 세기
사각형이 여러개인 경우 큰 사각형 출력

1을 만났을 때 기준으로 오른쪽 1의 개수 x 아래쪽 1의 개수
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                s = 0           # 사각형 넓이
                # 오른쪽 길이