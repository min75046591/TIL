def f(i, k, t):  # k개의 원소를 가진 배열 A, 부분집합 합이 t인 경우
    if i == k:   # 모든 원소에 대해 결정하면
        ss = 0   # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:    # 'bit[i] ==1' 에서 뒤의 ==1을 생략한 것이며, A[i]가 포함된 경우
                ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]:    # A[j]가 포함된 경우
                    print(A[j], end = ' ') 
            print()     # 부분집합 출력 
    
    else:
        for j in range(1, -1, -1):  # range(start, stop, step)
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)


N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*N  # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 10)