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