T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = []
    for i in range(N):  # N개의 피자를 화덕에 넣기 (실제로는 번호만 넣기)
        oven.append(i)
    next = N            # 대기중인 피자 인덱스

    tmp = -1
    while oven:
        tmp = oven.pop(0)   # 입구의 피자(번호)를 꺼내
        pizza[tmp] //= 2    # 한바퀴 회전 후 치즈량
        if pizza[tmp] > 0:  # 치즈가 남은 경우 다시 투입(인덱스 번호만)
            oven.append(tmp)

        elif next < M:  # 치즈가 다 놓고 다음 피자가 있으면
            oven.append(next)  # 대기중인 피자(번호) 넣기
            next += 1
    print(f'#{tc} {tmp+1}')