di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, cnt, work):
    global max_len
    if max_len < cnt:
        max_len = cnt

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if tops[i][j] > tops[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1, work)
                visited[ni][nj] = 0  # 백트래킹 -> 방문표시 초기화
            else:
                # 깎은 후의 봉우리 높이가 현재 봉우리 높이보다 작아야 함
                for l in range(1, K + 1):
                    if work == 1 and tops[ni][nj] - l < tops[i][j]:
                        original_height = tops[ni][nj]  # 원래 높이 저장
                        tops[ni][nj] -= l  # 봉우리 깎기
                        visited[ni][nj] = 1
                        dfs(ni, nj, cnt + 1, work - 1)
                        visited[ni][nj] = 0  # 백트래킹 -> 방문표시 초기화
                        tops[ni][nj] = original_height  # 깎은 봉우리 복구

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    tops = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_len = 0  # 등산로 최대 길이
    m_top = 0  # 가장 높은 봉우리

    # 최대 높이 구하기
    for p in range(N):
        for q in range(N):
            if m_top < tops[p][q]:
                m_top = tops[p][q]

    # 최대 높이와 같은 봉우리들의 위치 넣기
    for k in range(N):
        for l in range(N):
            if tops[k][l] == m_top:
                visited[k][l] = 1
                dfs(k, l, 1, 1)

    print(f'#{tc} {max_len}')
