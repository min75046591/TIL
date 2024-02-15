T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 화덕 크기, M 피자 개수
    pizza = list(map(int, input().split()))  # 각 피자의 치즈의 양

    last = 0  # 화덕에 들어갈 피자 인덱스 (front)
    oven_size = N + 1
    oven = [0] * (N + 1)  # 순환큐, front는 비워둠
    front = rear = 0
    for i in range(N):  # 화덕에 피자(인덱스) 투입
        rear += 1
        oven[rear] = i
        last += 1

    tmp = -1  # 치즈를 확인중인 피자(인덱스)
    while front != rear:  # 오븐(순환큐)가 비워질 때 까지
        front = (front + 1) % oven_size  # 먼저 투입된 피자순으로 꺼내서(dequeue)
        tmp = oven[front]
        pizza[tmp] //= 2
        if pizza[tmp] > 0:  # 치즈가 남아있으면 재투입
            rear = (rear + 1) % oven_size
            oven[rear] = tmp
        elif last < M:  # 치즈가 다 녹았고, 대기중인 피자(인덱스)가 있으면
            rear = (rear + 1) % oven_size
            oven[rear] = last
            last += 1  # 치즈가 0으로 초기화된 경우, 투입될 피자(인덱스)
    print(f'#{tc} {tmp + 1}')  # 인덱스 -> 피자 번호