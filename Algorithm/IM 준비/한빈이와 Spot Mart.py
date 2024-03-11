"""
과자 두 봉지를 사서 양손에 하나씩
N개의 과자 봉지
M 들고 갈 수 있는 최대 무게

각 a그램의 무게

최대 무게 합 => 무조건 두 봉지

들고 갈 방법이 없으면 -1 출력
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 0  # 왼손
    right = 0  # 오른손
    max_v = -1
    for i in range(N-1):
        left = arr[i]
        for j in range(i+1, N):
            right = arr[j]
            sum_v = left + right
            if max_v < sum_v and sum_v <= M:
                max_v = sum_v

    print(f'#{tc} {max_v}')