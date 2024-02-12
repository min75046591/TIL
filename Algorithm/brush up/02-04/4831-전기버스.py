T = int(input())
for tc in range(1, T+1):
    # K는 한번에 이동할 수 있는 숫자
    # N은 종점. M은 정류장의 개수
    K, N, M = map(int, input().split())
    bus_stop_list = [0] + list(map(int, input().split())) + [N]

    # 마지막으로 충전한 장소 기억
    last = 0
    # 충전한 횟수 기억
    cnt = 0
    # for i -> M 정류장을 하나씩 들리면서, 다음 정류장으로 이동 가능한지 확인
    for i in range(1, M+2):
        if bus_stop_list[i-1] + K < bus_stop_list[i]:
            cnt = 0
            break
        elif last + K < bus_stop_list[i]:
            cnt += 1
            last = bus_stop_list[i-1]
    print(f'#{tc} {cnt}')