T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 정수의 개수, M 구간의 개수
    nums = list(map(int, input().split()))
    sum_list = []   # 구간합을 모을 리스트
    for i in range(N-M+1):
        sum_nums = 0
        for j in range(M):
            sum_nums += nums[i+j]
        sum_list.append(sum_nums)
    
# 가장 큰 합과 가장 작은 합의 차
    max_num = 0
    min_num = 10000*N
    for k in sum_list:
        if max_num < k:
            max_num = k
        if min_num > k:
            min_num = k
        result = max_num - min_num

    print(f'#{tc} {result}')