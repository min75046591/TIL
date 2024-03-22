"""
C++ 1초(1억번) => 1 tc당 천만번

문제 키워드
- 선반 높이 B
- 키
-> B보다 작아서, 탑을 쌓을거야
    -> 탑의 높이 : 점원들의 키(H)의 합

-> 경우의 수를 모두 보면 될까?

2. 알고리즘
- DFS + 백트래킹
=> 시간복잡도 ?
-> 20! ==> 가지치기가 많이 되는거 같긴 한데..
            단순한 DFS로는 가능한지 모르겠다!
       ==> 똑같은 로직으로 다르게 구현할 수 있나?
            -> 자료 구조를 바꿀 수 있나?
            -> 접근법을 조금 바꿀 수 없나?

중복을 제거한 조합 문제 -> 이진트리로 생각하면 좋음
-> 2^20 == 백만번
            
최악의 경우 20!
-> 가지치기 생각하기 (중복 제거)
"""
def dfs(cnt, sum_height):
    global ans
    # 기저조건
    # 1. 키의 합이 B 이상이면 종료
    # -> 현재까지 쌓은 탑의 높이
    if sum_height >= B:
        # 제일 높이가 낮은 탑이 정답
        # - 최소 탑의 높이는 재귀호출함수들이 "동시에" 사용함 -> 전역변수로 사용
        ans = min(ans, sum_height)
        return

    # 2. 모든 점원이 탑을 쌓았다면 종료
        # -> 현재까지 쌓은 점원의 수(cnt)
    if cnt == N:
        return

    # 재귀호출파트
    # 쌓는다
    dfs(cnt+1, sum_height+arr[cnt])
    # 안쌓는다
    dfs(cnt+1, sum_height)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    dfs(0,0)
    print(f'#{tc} {abs(ans-B)}')