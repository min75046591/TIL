"""
같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출

한 조의 인원에 제한 없음. 한 사람이 여러 장의 종이를 제출하거나
여러 사람이 한 사람을 지목한 경우 모두 같은 조가 됌.

1-2, 1-3 이라면 1-2-3이 같은 조. 즉 부모가 같으면 같은 조.

번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성.
"""
def find_set(x):
    while x != p[x]:    # 자기 자신을 가리키면(p[x]==x) 대표원소
        x = p[x]
    return x

def union(a, b):
    # p[b]= a  ->  금지! 뚝 잘라질 수 있음
    p[find_set(b)] = find_set(a)    # b의 대표원소가 자기자신 대신 a의 대표원소를 가리키도록 바꿈

"""
def find_set_r(x):  # 재귀로 푸는 법. 참고
    if x == p[x]:
        return x
    else:
        p[x] = find_set_r(p[x]) # path compression
        return p[x]
"""

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    p = [i for i in range(N+1)] # 각자 대표원소 make_set(i) ~ make_set(N)
    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)

    cnt = 0
    for i in range(1, N+1):
        if i == p[i]:   # 대표원소인 경우
            cnt += 1

    print(f'#{tc} {cnt}')