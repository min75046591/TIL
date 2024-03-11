"""
공의 개수의 최솟값을 구하라
서로 다른 두 공이 겹치지 않는다
공이 조금만 보여도 카운트
"""
# ver.1
'''
T = int(input())
for tc in range(1, T+1):
    arr = input()
    cnt = 0
    for i in range(len(arr)-1):

        if arr[i:i+2] == '(|' or arr[i:i+2] == '|)' or arr[i:i+2] == '()':
            cnt += 1
'''
# ver.2
T = int(input())
for tc in range(1, T+1):
    arr = input()
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] == '(':
            if arr[i+1] == '|':
                cnt += 1
            elif arr[i+1] == ')':
                cnt += 1

        elif arr[i] == '|':
            if arr[i+1] == ')':
                cnt += 1

    print(f'#{tc} {cnt}')