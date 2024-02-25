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
            ni, nj = i, j
            if arr[i][j] == 1:
                # 가로 길이
                while ni < N and arr[i][nj] != 0:
                    nj += 1
                w = nj - j

                # 세로 길이
                while nj < N and arr[ni][j] != 0:
                    ni += 1
                l = ni - i

                result = w * l

                if max_v < result:
                    max_v = result
    print(f'#{tc} {max_v}')