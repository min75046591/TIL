"""
4 x 4 크기의 격자판 0부터 9 사이의 숫자 적혀있음

격자판 임의의 위치에서 시작, 동서남북 네 방향으로 인접한 격자로 총 6번 이동하면서
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수

한 번 거쳤던 격자칸을 다시 거쳐도 됨. -> 중복 가능
격자판 벗어나는 이동은 안됌

서로 다른 일곱 자리 수들의 개수를 구하라!
"""
import sys
sys.stdin = open("input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, s):
    global cnt
    if len(s) == 7:
        result.add(s)
        return

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<4 and 0<=nj<4:
            dfs(ni, nj, s + arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    cnt = 0
    result = set()      # 중복 제거
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')