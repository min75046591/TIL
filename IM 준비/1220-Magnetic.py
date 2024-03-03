# 스택으로 구현 가능!
# 열 검사 함수
# red = 1, blue = 2
# def get_sero_cnt(col):
#     cnt = 0
#     # red 자성체를 체크
#     is_red = False
#
#     for row in range(N):
#         # 1. red 자성체 발견
#         if arr[row][col] == 1:
#             is_red = True
#         # 2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt += 1
#         elif is_red and arr[row][col] == 2:
#             cnt += 1
#             is_red = False  # 갱신
#     return cnt
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     total_cnt = 0
#     # 열 순회하면서 total_count 누적
#     for col in range(N):
#         total_cnt += get_sero_cnt(col)
#     print(f'#{tc} {total_cnt}')

"""
1 은 N극 성질을 갖는 자성체 = 빨강색
2 는 S극 성질을 갖는 자성체 = 파란색
윗부분이 N극 아래부분이 S극

충돌한 상태 = 빨강 아래에 파랑이 있을때
"""
T = 10
for tc in range(1, T+1):
    N = int(input())    # 한 변의 길이
    arr = [[list(map(int, input().split()))] for _ in range(N)]
    stack = []
    cnt = 0     # 충돌 횟수
    for i in range(N):
        for j in range(N):
            # 빨강만 줍기
            if arr[j][i] == 1:
                stack.append(i)


