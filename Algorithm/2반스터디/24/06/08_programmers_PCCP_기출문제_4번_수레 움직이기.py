"""
n x m 크기 격자 모양의 퍼즐판
빨간색 수레와 파란색 수레를 각 자신의 도착칸에 도착해야함
각 턴마다 반드시 모든 수레를 상하좌우로 인접한 칸 중 한 칸으로 움직여야함
벽이나 격자 판 밖 x
방문했던 칸 x
도착 칸에 위치한 수레는 움직일 수 없음. 해당 칸에 고정
동시에 두 수레를 같은 칸으로 움직일 수 없음
수레끼리 자리 바꾸기 못함
"""

# 20개중 5개 정답

from collections import deque

def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    # 방향 벡터 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 시작 지점과 도착 지점 찾기
    red_start = blue_start = red_goal = blue_goal = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_goal = (i, j)
            elif maze[i][j] == 4:
                blue_goal = (i, j)
    
    # BFS 초기화
    queue = deque([(red_start, blue_start, 0)])
    visited = set()
    visited.add((red_start, blue_start))
    
    while queue:
        red_pos, blue_pos, turns = queue.popleft()
        
        # 두 수레가 모두 도착 지점에 도착했는지 확인
        if red_pos == red_goal and blue_pos == blue_goal:
            return turns
        
        for dr, dc in directions:
            new_red_pos = (red_pos[0] + dr, red_pos[1] + dc)
            new_blue_pos = (blue_pos[0] + dr, blue_pos[1] + dc)
            
            # 빨간 수레 이동 가능 여부 체크
            if not (0 <= new_red_pos[0] < n and 0 <= new_red_pos[1] < m and maze[new_red_pos[0]][new_red_pos[1]] != 5):
                new_red_pos = red_pos
            
            # 파란 수레 이동 가능 여부 체크
            if not (0 <= new_blue_pos[0] < n and 0 <= new_blue_pos[1] < m and maze[new_blue_pos[0]][new_blue_pos[1]] != 5):
                new_blue_pos = blue_pos
            
            # 두 수레가 같은 칸에 도달하는 경우를 방지
            if new_red_pos != new_blue_pos and (new_red_pos, new_blue_pos) not in visited:
                visited.add((new_red_pos, new_blue_pos))
                queue.append((new_red_pos, new_blue_pos, turns + 1))
    
    return 0