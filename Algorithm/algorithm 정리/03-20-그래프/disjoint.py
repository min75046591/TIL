"""
1~6번까지 노드가 존재
"""
# 1. make_set
def make_set(n):
    # 자기자신이 대표인 데이터 6개가 리스트로 생성. 1~6사용
    # [0, 1, 2, 3, 4, 5, 6]
    return [i for i in range(n)]   

# 1~6번까지를 사용하기 위해 7개
parents = make_set(7)

# 2. find_set: 대표자를 찾아보자
"""
부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
언제까지? -> 자기 자신이 대표인 데이터를 찾을 때 까지
"""
def find_set(x):
    # 자기 자신이 대표네? -> 끝
    if parents[x] == x:
        return x
    
    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    return find_set(parents[x])

# 3. union
def union(x, y):    # 두 개를 합치라는 의미
   # parents[y] = x  -> y의 대표자는 x이다 라는 의미
    # 이미 연결되어 있는 친구들끼리 한번 더 연결 시도하면 cycle 발생
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

union(1, 3)
union(2, 3)
union(5, 6)