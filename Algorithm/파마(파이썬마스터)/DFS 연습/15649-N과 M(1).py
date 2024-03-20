"""
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
N, M = list(map(int, input().split()))
visited = [0]*N
result = []

def dfs(r, n, m):
    if r == m:
        print(*result)
        return

    for i in range(N):
        if visited[i] == 0:
            result.append(i+1)
            visited[i] = 1
            dfs(r+1, n, m)
            visited[i] = 0
            result.pop()

dfs(0, N, M)




