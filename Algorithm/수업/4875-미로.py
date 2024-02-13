"""
NxN 크기의 미로
도착할 수 있으면 1, 아니면 0
2 : 시작점
3: 도착점
0 : 통로
1 : 벽
미로 표시의 방법은 방문한 곳은 벽으로 메꿔버리기
"""


def f(i, j, N):
    stack = []  # 지나간 경로 저장

    while True:
        maze[i][j] = 1  # 방문한 칸에 표시하기
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]: # 상하좌우 탐색
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1: # 미로 내부 and 벽이 아니면
                if maze[ni][nj] == 3:
                    return 1
                stack.append((i,j)) # 현재칸 push
                i, j = ni, nj
                break   # for di, dj / 새 i, j 칸으로 이동
        else:    # 지나온 경로에서 다시 시작해야 하는 경우
            if stack:
                i, j = stack.pop()
            else:
                return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    sti = stj = -1   # 값이 -1 이라는 것은 시작점을 아직 찾지 않았음을 의미
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                sti = i
                stj = j
                break   # for j
        if sti != -1:       # 시작점을 찾았으면
            break   # for i
    # 미로찾기
    """
    시작점을 찾았으면 이제 f 함수를 호출하여 DFS(깊이 우선 탐색)를 통해 도착점에 도달할 수 있는지 확인합니다. 
    시작점의 행과 열, 그리고 미로의 크기 N을 인자로 전달합니다.
    """
    result = f(sti, stj, N)
    print(f'#{tc} {result}')