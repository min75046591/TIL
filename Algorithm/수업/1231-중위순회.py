"""
in -order 형식
트리를 순회했을때 나오는 단어를 출력
정점 번호는 위에서 아래로. 왼쪽에서 오른쪽으로
루트 정점의 번호는 항상 1

완전 이진트리는 중간에 빈칸이 없다
"""
def in_order(T):
    if T:
        in_order(left[T])
        result.append(arr[T-1][1])
        in_order(right[T])

for tc in range(1,11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
# for문을 돌면서 배열 번호에 따라 영어 저장
    left = [0] * (N+1)      # 부모 인덱스를 저장할 왼쪽 자식 배열
    right = [0] * (N+1)     # 부모 인덱스를 저장할 오른쪽 자식 배열
    tree = [0] * (N+1)      # 자식 인덱스를 저장할 부모 배열
    result = []

    for i in range(N):
        # 현재 노드의 왼쪽 자식 노드를 설정
        if len(arr[i]) >= 3:
            left[int(arr[i][0])] = int(arr[i][2])
            tree[int(arr[i][2])] = int(arr[i][0])
        # 현재 노드의 정보가 오른쪽 자식을 가지고 있는 경우를 확인
        if len(arr[i]) >= 4:
            right[int(arr[i][0])] = int(arr[i][3])
            tree[int(arr[i][3])] = int(arr[i][0])

    in_order(1)

    print(f'#{tc}', ''.join(result))

# 강사님 버전
def in_order(T, N):
    if T<=N:             # 존재하는 노드면
        in_order(T*2, N)            # 왼쪽자식 방문
        print(tree[T], end = '')    # 부모노드 처리
        in_order(T*2+1, N)          # 오른쪽 자식 방문

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)            # N번까지 있고, 노드가 비어있는 완전이진트리
    for _ in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]
    print(f'#{tc}', end = ' ')
    in_order(1, N)
    print()














