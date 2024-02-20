"""
노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내라
부모가 없는 노드가 전체의 루트 노드 = 당연한 말
"""
def pre_order(N):
    global cnt
    if N:     # N에 요소가 남아있다면
        cnt += 1
        pre_order(left[N])
        pre_order(right[N])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())   # E 간선의 개수, N 서브트리
    arr = list(map(int, input().split()))
    left = [0]*(E+2)                    # 부모를 인덱스로 자식 저장, 간선개수 + 1 = 노드 개수
    right = [0]*(E+2)                   # 리스트의 0을 사용하지 않기 위해 +1 따라서 E+2
    parents = [0]*(E+2)                 # 자식을 인덱스로 부모 저장

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]     # 쌍으로 받은 값에서 첫번째가 부모 값, 두 번째가 자식값
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parents[c] = p
    cnt = 0
    print(f'#{tc}', pre_order(N))