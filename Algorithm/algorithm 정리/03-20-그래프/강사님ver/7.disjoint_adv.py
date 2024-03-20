def make_set(n):
    parent = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
    rank = [0] * n  # 트리의 깊이(랭크)를 저장
    return parent, rank

parent, rank = make_set(7)


def find_set( x):
    if parent[x] == x:
        return x

    return find_set(parent[x])

    # 경로 압축 (path compression)을 통해 부모를 루트로 설정
    # self.parent[x] = self.find_set(self.parent[x])
    # return self.parent[x]

def union( x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        # 랭크를 비교하여 더 높은 트리의 루트를 부모로 설정
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# 예제 사용법
n = 5  # 원소의 개수

union(1, 3)
union(2, 3)
union(5, 6)

print(parent)

target_x = 1
target_y = 3

# 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
if find_set(target_x) == find_set(target_y):
    print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
else:
    print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")
