def f(r, s):            # 횟수, 성공할 확률들의 합
    global max_v
    if r == N:       # 모든 경우를 다 고려했을 때
        if max_v < s:
            max_v = s
            return
    if max_v > s:       # 현재까지의 결과가 최대값보다 작으면 더 이상 진행할 필요 없음
        return

    for i in range(N):
        if visited[i] == 0 and arr[r][i]: #  방문하지 않았고 그 칸의 숫자가 0이 아닐 때
            visited[i] = 1  # 방문 표시
            f(r+1, s*arr[r][i]*0.01)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0   # 최대 성공할 확률
    visited = [0]*N
    f(0, 1)         # s가 0이면 곱해도 계속 0이라 1로 해줘야함.
    print(f'#{tc} {max_v*100:6f}')