"""
W 흰색
B 파란색
R 빨간색

새로 칠해야 하는 칸의 개수의 최솟값을 구하라
"""

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 줄의 개수, M 한 줄당 문자의 개수
    arr = [input() for _ in range(N)]
    min_v = N*M
    # 그 라인에 다른 색깔이 있다면 x로 바꾸기
    # 마지막에 x의 개수를 세서 최소개수 구하기]
    for i in range(N-2):    # W 영역의 마지막 행
        for j in range(N-1):   # B 영역의 마지막 행
            cnt = 0
            for p in range(N):   # 줄의 개수 만큼
                for q in range(M):  # 한 줄 당 문자의 개수
                    if p <= i and arr[p][q] != 'W':
                        cnt += 1
                    elif i < p <= j and arr[p][q] != 'B':
                        cnt += 1
                    elif j < p and arr[p][q] != 'R':
                        cnt += 1
            if min_v > cnt:
                min_v = cnt
    print(f'#{tc} {min_v}')