"""
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 가능
"""
def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        result.append(i)
        dfs()
        result.pop()

N, M = map(int, input().split())
result = []
dfs()