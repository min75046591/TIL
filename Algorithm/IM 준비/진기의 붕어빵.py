def start(n, m, k):
    sold_bread = 0
    for person in p_time:
        # 공식, 특정 시간에 만들 수 있는 빵의 개수
        made_bread = (person // m) * k

        # 빵을 1개 팔았다
        sold_bread += 1

        # 재고 계산
        remain = made_bread - sold_bread

        # 재고가 0보다 작으면 실패
        if remain < 0:
            return 'impossible'
    # 실패가 없었으면 성공공
    return 'possible'


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # M초에 K개의 붕어빵, N 사람 인원
    p_time = list(map(int, input().split()))  # 손님 도착시간
    p_time.sort()   # 손님 도착 시간 오름차순
    print(f'#{tc} {start(N, M, K)}')

"""
울 강사님 ver
def f(N, M, K):
    cnt = 0
    for i in range(N):
        if t[i]//M*K  < i+1:   # t[i] 시간의 생산량, t[i] 시간까지 도착한 손님 수 i+1
            return 'Impossible'
    return 'Possible'
 
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N 명의 손님, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음.
    t = list(map(int, input().split()))
    t.sort()    # 도착 시간순으로 정렬
    print(f'#{tc} {f(N, M, K)}')
"""