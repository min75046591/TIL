# 가장 큰 수는 어디에 들어있을까...
N = 5
arr = [1, 3, 2, 5, 4] # 같은 숫자가 없는 경우

max_idx = 0
for i in range(1, N):
    if arr[max_idx] < arr[i]:  # arr[i]가 더 크면
        max_idx = i            # 최댓값의 위치를 i로 변경
    # if arr[max_idx] <= arr[i]:     # <= 최댓값이 여러개인 경우 가장 오른쪽
    # max_id = i                     # 최댓값의 위치를 i로 변경