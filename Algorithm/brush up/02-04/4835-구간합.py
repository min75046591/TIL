'''
각 구간을 처음 인덱스 부터 M 만큼씩 더하여 max_v 값에 저장
그 이후 max_v에서 max 값을 구하여 출력
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = 10000*N
    for i in range(N-M+1): # M개의 값을 더하기 시작할 위치 선정
        sum = 0  #
        for j in range(M):
            sum += arr[i+j] # 이웃한 M개의 값 더하기
        # 최고값과 최저값 구하기
        if max_sum < sum:
            max_sum = sum

        if min_sum > sum:
            min_sum = sum

    result = max_sum - min_sum
    print(f'#{tc} {result}')





