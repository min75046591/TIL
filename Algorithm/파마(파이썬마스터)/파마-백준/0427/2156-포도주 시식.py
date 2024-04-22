"""
포도주 잔이 일렬로 놓여있음
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야함
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없음

1부터 n까지 순서대로 번호가 붙어져있음
될 수 있는 대로 많은 양의 포도주를 마셔야 함

양이 많은 순서 대로 집고 만약 연속으로 해당하는 인덱스는 제외
"""
# 리커젼 에러
def dfs(index, count, total):
    global max_total

    if count >= 3:  # 연속으로 3잔을 마신 경우
        return

    if index >= N-1:  # 마지막 포도주까지 고려했을 때
        max_total = max(max_total, total)
        return

    # 현재 포도주를 마시는 경우
    dfs(index + 1, count + 1, total + wines[index])
    # 현재 포도주를 마시지 않는 경우
    dfs(index + 1, 0, total)


N = int(input())
wines = [int(input()) for _ in range(N)]  # [6, 10, 13, 9, 8, 1]
max_total = 0
dfs(0, 0, 0)
print(max_total)


# 정답 코드

def max_wine(n, wines):
    dp = [0] * (n + 1)

    # 첫 번째 잔의 경우
    dp[1] = wines[0]

    # 두 번째 잔의 경우
    if n >= 2:
        dp[2] = wines[0] + wines[1]

    # 세 번째 잔부터는 두 가지 경우를 고려하여 최대값을 선택
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + wines[i - 1], dp[i - 3] + wines[i - 2] + wines[i - 1])

    return dp[n]

n = int(input())
wines = [int(input()) for _ in range(n)]
print(max_wine(n, wines))
