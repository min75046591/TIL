"""
1부터 N까지 자연수 중 M개를 고른 수열
같은 수를 여러 번 골라도 됨
고른 수열은 비내림차순 -> 오름차순
중복되는 수열은 출력 x
"""
def dfs(start):
    if len(result)==M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N+1):
            result.append(i)
            dfs(i)
            result.pop()

N, M = map(int, input().split())
result = []
dfs(1)