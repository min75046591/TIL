'''
집합 A의 부분 집합 중 N개의 원소를 갖고 그 합이 K인 부분집합의 개수를 구해라
해당하는 부분집합이 없는 경우 0을 출력.
'''
T = int(input())
for tc in range(1, T+1):
    i <= 12
    def f(arr, N):
        for i in range(1, 1 << N):
            s = 0
            for j in range(N):
                if i & (1 << j):
                    s += arr[j]
                    #print(arr[j], end=' ')
            #print(s)
            if s == 0:
                return True
        return False

    N = int(input())
    arr = list(map(int, input().split()))
    print(f(arr, N))