"""
# N x N
# 1 -> 0 / 0 -> 1 로 바뀌는게 토글
# 각 칸의 숫자는 M초까지 1초마다 조건에 따라 토글됨
#
# 1) k초가 되는 순간, i+k 가 같거나 k의 배수가 되는 영역은 토글
# 2) M이 k의 배수인 경우와 M초에는 1)을 따르는 대신 전체가 토글
#
# M초 후 1인 영역의 개수를 출력
# """
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # M 몇초인지
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for k in range(1, M+1):  # M 초 시간동안
        for i in range(N):
            for j in range(N):
                # M이 k의 배수일 때 전체 토글
                if M % k == 0:
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    elif arr[i][j] == 0:
                        arr[i][j] = 1

                # k초일때 i+j==k 이거나 k의 배수가 되는 영역은 토글
                elif (i+1) + (j+1) == k or ((i+1) + (j+1)) % k == 0:
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    elif arr[i][j] == 0:
                        arr[i][j] = 1
    # 토글 후 1 개수
    for p in range(N):
        for q in range(N):
            if arr[p][q] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')