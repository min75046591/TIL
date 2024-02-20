"""
1부터 N까지 자연수를 이진 탐색 트리에 저장

전위 순회에
중위 순회값 넣기

완전 이진 트리가 되도록

이진 탐색 트리의 루트에 저장된 값과, N//2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력

"""
def make_tree(t):
    global number
    # 배열이니까 배열크기 넘어가지 않도록
    if t <= N:
        # 왼쪽노드는 현재 인덱스의 2배
        tree[t] = number
        # 값 넣었으면 증가시키기
        number += 1
        # 우측 노드는 인덱스 2배 + 1
        make_tree(t*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0 for i in range(N+1)]
    number = 1
    make_tree(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
