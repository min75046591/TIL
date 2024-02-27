"""
N x N 칸 오른쪽이나 아래로만 이동 가능
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계의 최소
모든 경로에 대한 합을 계산하고 그 중 최소값 찾기

완전탐색 + 재귀
"""
def f(i, j, s):     # i좌표, j좌표, s 누적합
    global min_v
    if s > min_v:   # 누적합 s가 최소값보다 크면
        return
    if i == N or j == N:    # i, j가 범위를 벗어난 경우
        return
    if (i, j) == (N-1, N-1):
        s += arr[i][j]
        if min_v > s:
            min_v = s
        return

    if not visited[i][j]:   # 현재 위치를 방문한적 없다면
        visited[i][j] = 1   # 방문 표시
        f(i+1, j, s+arr[i][j])  # 방문한 위치를 기준으로 오른쪽과 아래로 이동하여 재귀호출 실행
        f(i, j+1, s+arr[i][j])
        visited[i][j] = 0       # 다시 이전 위치로 돌아가기 위해 현재 방문 위치를 0으로 되돌림

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_v = 1000
    f(0, 0, 0)
    print(f'#{tc} {min_v}')