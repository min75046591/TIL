'''
12개의 원소를 가지고 있는 집합의 부분집합 수는 2**12-1 개 이다.
각 원소가 존재하거나 안하거나 2개의 경우의 수가 12번이 반복되고
모두 존재하지 않는 경우는 빼야 하므로 -1을 해준다.
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = 0  # 부분집합의 개수

    new_list = []
    for i in range(1 << 12):  # 1 << n: 부분 집합의 개수
        tmp = []
        for j in range(12):  # 원소의 수만큼 비트를 비교
            if i & (1 << j): # i의 j번 비트가 1인 경우
                tmp.append(A[j])

        if len(tmp) == N and sum(tmp) == K:
            result += 1

    print(f'#{tc} {result}')

