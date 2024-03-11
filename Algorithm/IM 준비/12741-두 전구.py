"""
100초에서 겹치는 초를 구하라
"""
T = int(input())
result = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    sum_v = min(B, D) - max(A, C)
    if sum_v < 0:
        sum_v = 0
    result.append(sum_v)

for tc in range(1, T+1):
    print(f'#{tc} {result[tc-1]}')