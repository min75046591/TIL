'''
집합 A = 1부터 12까지의 숫자
N개의 원소
원소의 합이 K
부분 집합의 개수를 출력
없는 경우 0을 출력
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = 0    # 부분집합의 개수
    new_list = []

    for i in range(1<<12): # A 세트의 모든 가능한 부분집합을 순회 
        tmp = []
        for j in range(1<<12): # 현재 부분 집합에서 모든 가능한 요소를 순회
            if i & (1<<j): # 현재 부분 집합에 j번째 요소가 있는지 확인
                tmp.append(A[j])

        if len(tmp) == N and sum(tmp) == K:
            result += 1
    print(f'#{tc} {result}')