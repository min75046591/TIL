"""
N*N개의 벌통이 정사각형 모양으로 배치
각 칸의 숫자는 벌통에 있는 꿀의 양

각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택하고, 선택한 벌통에서 꿀을 채취 가능
단 서로 겹치면 안됨.

서로 다른 벌통에서 채취한 꿀이 섞이면 안됨. 따라서 하나의 벌통에서 채취한 꿀은 하나의 용기에 담음
한번 채취한 꿀은 벌통에 있는 모든 꿀을 한번에 채취함.
두 일꾼이 채취할 수 있는 꿀의 최대 양은 C.

벌통 크기 = N, 선택할 수 있는 벌통의 개수 = M, 채취 가능한 최대 꿀의 양 = C
"""
import sys
sys.stdin = open(input.txt)

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honey_map = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0   # 최대 수익
    
    # 같은 행에 있다면 겹치면 안됨.
    # 첫 번째 양봉업자를 기준으로 두 번째 양봉업자와 비교
    # 단 같은 행 일땐 겹치면 안되고, 맵 밖으로 나가면 안됌. 숫자가 더했을때 C이하이면서 가장 큰 합

    # 첫 번째 양봉업자
    for i in range(N):
        for j in range(N):
            sum_a = []
            for k in range(C):
                sum_a += honey_map[i][j+k]

            # 두 번째 양봉업자
            for p in range(N):
                for q in range(j+C, N):
                    sum_b = []
                    for l in range(C):
                        if N-(j+C) >= C:    # 맵 밖으로 나가지 않고 겹치지 않는 경우
                            sum_b += honey_map[p][q+l]

            # 꿀 계산





    # 다른 행이라면 어디든 상관 없음