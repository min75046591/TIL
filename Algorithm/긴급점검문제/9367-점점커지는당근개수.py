"""
연속으로 커지는 당근의 갯수중 최대
1씩 커지는게 아닌 연속으로 커지는것!
"""
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_v = 0
#     cnt = 1
#     for i in range(N-1):
#         if arr[i] < arr[i+1]:
#             cnt += 1
#         else:
#             cnt = 1
#         if max_v < cnt:
#             max_v = cnt
#     print(f'#{tc} {max_v}')
---------------------------------------------------
# 틀린 코드 - 1씩 연속이 아닌 그냥 연속으로 크면 됌
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_v = 0
#     for i in range(N-1):
#         if arr[i]+1 == arr[i+1]:
#             max_v = arr[i+1]
#         else:
#             max_v = 1
#     print(f'#{tc} {max_v}')
---------------------------------------------------
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    cnt = 1
    for i in range(1, N):
        if arr[i-1] < arr[i]:
            cnt += 1
        else:
            cnt = 1
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')