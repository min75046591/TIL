# 인접 행렬 DFS: 재귀
graph = [
    [0, 1, 0, 1, 0],     # 0번은 1, 3으로 갈 수 있다
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

visited = [0] * 5
path = []


def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다!

    # 다음 재귀 호출 전

    # 돌아 왔을 때 작업 -> 재귀호출 후 작업
    # visited[now] = 1
    # print(now, end=' ')
    
    
    # 다음 재귀 호출
    # dfs : 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    
    # 가기 전에 작업
    for to in range(5):
        # 갈 수 없다면 pass
        if graph[now][to] == 0:
            continue

        # 이미 방문했다면 pass
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)

# 출발점 초기화
visited[0] = 1
path.append(0)
# 호출
dfs(0)
print(path)
    
    # 돌아왔을 때 작업


print('-------------------------')


# 인접 리스트 DFS: 재귀
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]

visited = [0] * 5
path = []


def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다!

    # 다음 재귀 호출 전

    # 돌아 왔을 때 작업 -> 재귀호출 후 작업
    # visited[now] = 1
    # print(now, end=' ')
    
    
    # 다음 재귀 호출
    # dfs : 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    
    
    """
    # 인접 리스트

    차이점1. 갈 수 없는 곳 조건 필요없음
    
    차이점2. for 문 작성 수정
    """
    for to in graph[now]:

        # 이미 방문했다면 pass
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)


# 출발점 초기화
visited[0] = 1
path.append(0)
# 호출
dfs(0)
print(path)