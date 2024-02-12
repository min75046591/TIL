T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # K: 최대 이동거리, N : 종점번호, M: 충전기 개수
    charger = [0]+list(map(int, input().split())) +  [N] # 종점을 추가
    
    # last = charger[0] 으로 해도 무방
    last = 0  # 마지막 충전 위치
    count = 0 # 충전 횟수
    for i in range(1, M+2):  # 각 충전기 charger[i]에 대해
        if (charger[i] - charger[i-1])<=K:  # 첫번째 조건 -> 충전기 사이 운행 가능
            if (charger[i]-last)<=K:    # 충전기 사이 운행은 가능하나 마지막 충전기에서 너무 멀면
                last = charger[i-1]
                count += 1

        else:
            count = 0
            break
    print(f'#{tc} {count}')



    import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

        
    k, n, m  = map(int, input().split())
    charges = list(map(int, input().split()))

    stations = [0] * n

    # 충전기 있는자리 1 넣기
    for charge in charges :
        stations[charge] = 1

    # 그리디 : 매번 최선의 선택하면 최종적으로 최선의 정답
    # 최선의 선택 : 현 버스 위치에서 가장 먼 충전소 가기
    #(단, 다음 장소로 이동해야해서 갈수 있는 충전소 가는게 중요)
        
    # 버스 현재위치 pos
    pos = 0
    # 버스 충전횟수  cnt
    cnt = 0

    # 최선의 선택을 현재버스위치에서 k까지 갔을 때 N위치 넘는 경우(조건 -> while)

    while pos + k < n :
        # k 거리 내에서 가장 먼 충전소 찾아 위치이동
        # pos + K, pos + K-1, pos +k-2 ..., pos+1 탐색 순회
        for nxt in range(pos+k, pos-1, -1):
            # 다음 위치는 nxt
            # 다음 위치 nxt에서 충전소가 있다며 이동
            if stations[nxt] == 1 :
                pos = nxt
                cnt += 1
                break    # 중요!!!
        
        # 이 반복문이 끝나도 충전소 없는 경우(이동하지 않은 경우)
        if nxt == pos + 1:
            cnt = 0
            break

    print(f'#{test_case} {cnt}')




import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

        
    k, n, m  = map(int, input().split())
    charges = list(map(int, input().split()))

    stations = [0] * n

    # 충전기 있는자리 1 넣기
    for charge in charges :
        stations[charge] = 1

    # 그리디 : 매번 최선의 선택하면 최종적으로 최선의 정답
    # 최선의 선택 : 현 버스 위치에서 가장 먼 충전소 가기
    #(단, 다음 장소로 이동해야해서 갈수 있는 충전소 가는게 중요)
        
    # 버스 현재위치 pos
    pos = 0
    # 버스 충전횟수  cnt
    cnt = 0

    # 최선의 선택을 현재버스위치에서 k까지 갔을 때 N위치 넘는 경우(조건 -> while)

    while pos + k < n :
        # k 거리 내에서 가장 먼 충전소 찾아 위치이동
        # pos + K, pos + K-1, pos +k-2 ..., pos+1 탐색 순회
        for nxt in range(pos+k, pos-1, -1):
            # 다음 위치는 nxt
            # 다음 위치 nxt에서 충전소가 있다며 이동
            if stations[nxt] == 1 :
                pos = nxt
                cnt += 1
                break    # 중요!!!
        
        # 이 반복문이 끝나도 충전소 없는 경우(이동하지 않은 경우)
        else :
            cnt = 0
            break

    print(f'#{test_case} {cnt}')