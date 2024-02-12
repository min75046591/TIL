'''
K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
N : 종점 정류장
M : 충전기가 설치된 정류장 수
충전기 설치가 잘못되서 종점에 도착 할 수 없으면 0을 출력
출발지엔 항상 충전기가 설치됨. but 충전횟수 카운트 x
'''
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 0부터 N까지 버스 정류장중 충전기가 설치된 정류장
    bus_stop = [0] + list(map(int, input().split())) + [N]

    # 마지막으로 충전한 장소 기억
    last = 0
    # 충전 횟수
    cnt = 0
    # 정류장을 하나씩 들리면서 다음 정류장으로 이동 가능한지 확인
    for i in range(1, M+2):
    # 현재 정류장 이전에 설치된 충전기에서 충전하여 다음 정류장으로 이동 가능한 경우
        # bus_stop[i-1]는 현재 정류장의 바로 이전 정류장에 설치된 충전기의 위치
        if bus_stop[i-1] + K >= bus_stop[i]:
            continue
    # 마지막 충전 지점에서 다음 정류장으로 이동이 불가능하면
        elif last + K < bus_stop[i]:
    # 충전 횟수를 0으로 초기화하고 반복문을 종료
            cnt = 0
            break
        else:
    # 충전이 필요한 경우, 충전 횟수를 증가하고 마지막 충전 지점을 현재 정류장으로 갱신
            cnt += 1
            last = bus_stop[i-1]
    print(f'#{tc} {cnt}')