"""
1번부터 N번까지 N개의 상자를 갖고 있음
처음에는 상자에 모두 0으로 적혀있음
Q회동안 일정 범위의 연속한 상자를 동일한 숫자로 변경

Q번 동안 L번 상자부터 R번 상자까지의 값을 i로 변경

상자에 적혀있는 값들을 순서대로 출력
"""
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [-1] + [0]*N
    
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for k in range(L, R+1):
            arr[k] = i

    print(f'#{tc}', *arr[1:])