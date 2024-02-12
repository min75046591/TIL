T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_num, min_num = 1, 10 # 최대값과 최소값 설정
    for i in range(N):
        num = nums[i]
        # 최댓값이 여러개일 경우, 그 중 마지막 인덱스 구하기
        if max_num <= num:
            max_num = num
            max_num_index = i
        # 최솟값이 여러개일 경우, 그 중 첫번째 인덱스 구하기
        if min_num > num:
            min_num = num
            min_num_index = i

    index_gap = max_num_index - min_num_index
    if index_gap < 0:
        index_gap = - index_gap
    print(f'#{tc} {index_gap}')
