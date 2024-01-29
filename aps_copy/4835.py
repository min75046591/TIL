T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))  # 리스트를 바로 정렬합니다.

    # max_sum = sum(data[-m:])  # 최대값을 계산할 때 리스트 끝에서 m개 선택
    # min_sum = sum(data[:m])   # 최소값을 계산할 때 리스트 앞에서 m개 선택
    #
    # result = max_sum - min_sum
    
    sumlist = []

    # N개의 정수, 구간 M개
    for j in range(n - m + 1):  # 첫번째 수부터 마지막 위치 a-b+1까지 범위에서
        newSum = 0 # b개씩 묶기 위한 초기합 0으로 세팅
        for k in range(j, j + m):  # i부터 b번째 수까지(범위 b)로 해서 범위 내에서 구간 별로 묶음
            newSum += data[k]  # newSum에 할당해서 순회하며 각 구간 합 구함
        sumlist.append(newSum)  # newSum으로 구간 합 나타내고 구해진 값들을 sumList에 append함

    sumlist.sort() # sumList에 나타난 구간합들을 오름차순으로 정렬
    result = sumlist[-1] - sumlist[0] # 제일 적은 구간 합과 제일 큰 구간 합 사이의 값 차를 구함
    print(f'#{test_case} {result}')

    

    
    