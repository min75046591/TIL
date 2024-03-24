import sys
sys.stdin = open("input.txt", "r")

def dfs(cnt, s):
    global min_v
    # 종료 조건
    if s >= B:
        if s < min_v:
            min_v = s
            return
    if s > min_v:
        return
    if cnt == N:
        return

    dfs(cnt+1, s+arr[cnt])
    dfs(cnt+1, s)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 10001*N
    dfs(0, 0)
    print(f'#{tc} {abs(B-min_v)}')
