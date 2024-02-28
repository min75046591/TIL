"""
좌표 i에 꽃이 하나씩 심어져 있음
총 N개의 꽃
분무기는 정수 좌표에 놓을 수 있고, 좌표 x에 분무기를 놓으면 [X-D, X+D]에 심긴 꽃에 물을 줄 수 있다

N과 D가 주어질 때 모든 꽃이 한 개 이상의 분무기에 물을 받을 수 있게
최소한의 분무기 수를 구하라
"""
T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    cnt = 0
    if N % (D*2+1) == 0:
        cnt = N // (D*2+1)
    else:
        cnt = N // (D*2+1) + 1
    print(f'#{tc} {cnt}')