'''
작은 수는 먼저 나온 위치
큰 수는 마지막으로 나오는 위치
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = 0
    min_num = 101
    max_idx = 0  # 초기값 설정
    min_idx = 0  # 초기값 설정
    
    for i in range(N):
        if max_num <= nums[i]:  # 큰 수는 마지막 위치에 나온 수
            max_num = nums[i]
            max_idx = i    # 현재 인덱스 저장
        
        if min_num > nums[i]:     # 작은 수는 처음 위치에 나온 수
            min_num = nums[i]
            min_idx = i  # 현재 인덱스 저장


    idx_sum = max_idx - min_idx
    idx_sum = abs(idx_sum)

    print(f'#{tc} {idx_sum}')