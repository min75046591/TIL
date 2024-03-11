"""
집합 A의 부분 집합 중 N개의 원소를 갖고 있고
원소의 합이 K인 부분집합의 개수
"""
def f(i, M, N, K, s, c):  # s 부분집합의 합, c 부분집합 원소 개수
    global cnt
    if N == c and K == s:
        cnt += 1
    elif i == M:        # 끝까지 조사했을때
        return
    elif s > K or c > N:  # 부분집합의 합이 목표보다 크거나 더 많은 원소가 선택된 경우
        return
    else:
        f(i + 1, M, N, K, s + arr[i], c + 1)  # arr[i]가 포함되는 경우
        f(i + 1, M, N, K, s, c)  # arr[i]가 포함되지 않는 경우

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 원소의 개수 N, 합 K
    arr = [i for i in range(1, 13)]
    cnt = 0
    f(0, 12, N, K, 0, 0)
    print(f'#{tc} {cnt}')
