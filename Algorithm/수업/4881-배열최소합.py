# 순열 사용
def f(i, k, s):
    global min_v
    # 끝까지 순회하지 않았다면
    if i != k:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i] # 위치 교환
# 위치 교환 후 재귀적으로 다음위치로 이동, 현재까지 합에 새로 추가된 원소 +
            f(i+1, k, s+num_map[i][P[i]])
            P[i], P[j] = P[j], P[i] # 교환 전으로 복구
    # 끝까지 순회했을때
    elif i == k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_map = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]  # 0부터 N-1까지의 정수로 이루어진 리스트
    min_v = 100
    f(0, N, 0)
    print(f'#{tc} {min_v}')

# 강사님의 가지치기한 upgrade 버전
"""
def f(i, k, s): # i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i==k:
        # print(*P)
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):    # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i]<->P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]  # 교환전으로 복구
 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_v = 100
    cnt = 0
    f(0, N, 0)
    #print(f'#{tc} {min_v} {cnt}')
    print(f'#{tc} {min_v}')
"""