import sys
sys.stdin = open("input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, path):
    # 기저조건: 7자리면 끝
    if len(path) == 7:
        # 현재까지의 경로를 저장
        result.add(path)
        return

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        # 범위 밖으로 넘어가면 pass
        if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
            continue

        dfs(new_y, new_x, path + maps[new_y][new_x])


T = int(input())

for tc in range(1, T + 1):
    # 격자판 저장
    # maps = [list(map(int, input().split())) for _ in range(4)]
    # 갈 때 마다 경로를 더하기 위해서 문자열로 저장
    maps = [input().split() for _ in range(4)]
    # 중복을 제거하기 위해 set 사용
    result = set()

    # 시작 지점
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')
