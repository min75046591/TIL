"""
N 개의 정수. 최솟값과 최댓값을 구하라
"""
N = int(input())
arr = list(map(int, input().split()))
max_v = max(arr)
min_v = min(arr)

# max_v = 0
# min_v = 100000

# for i in range(N):
#     if max_v < arr[i]:
#         max_v = arr[i]
#
#     if min_v > arr[i]:
#         min_v = arr[i]

print(min_v, max_v)