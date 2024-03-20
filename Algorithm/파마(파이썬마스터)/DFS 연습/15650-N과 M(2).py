"""
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순
"""
def dfs(start):
    if len(result)==M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()

N, M = map(int, input().split())
result = []
dfs(1)