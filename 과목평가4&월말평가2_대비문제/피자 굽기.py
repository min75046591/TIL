"""
N개의 피자를 동시에 구울 수 있는 화덕
피자는 치즈가 모두 녹으면 화덕에서 꺼냄
치즈의 양은 피자마다 다르다
따라서 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는
순서는 바뀔 수 있다.

화덕에 가장 마지막까지 남아있는 피자 번호를 출력

입구는 하나
넣거나 뺄 수 있다.
한바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다
c//2
치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에
남은 피자를 순서대로 넣는다
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 화덕 크기, M 피자 개수
    pizza = list(map(int, input().split())) # 각 피자 치즈의 양

    last = 0    # 화덕에 들어갈 피자 인덱스 (front)
    oven_size = N+1
    oven = [0]*(N+1)    # 순환큐, front는 비워둠
    front = rear = 0
    for i in range(N):
        rear += 1
        oven[rear] = i
        last += 1

    tmp = -1    # 치즈를 확인중인 피자(인덱스)
    while front != rear:    # 오븐(순환큐)가 비워질 때 까지
        front = (front+1)%oven_size # 먼저 투입된 피자순으로 꺼내서(dequeue)
        tmp = oven[front]
        pizza[tmp] //= 2

        if pizza[tmp] > 0:  # 치즈가 남아 있으면 재투입
            rear = (rear+1)%oven_size
            oven[rear] = tmp
        elif last < M:  # 치즈가 다 녹았고, 대기중인 피자(인덱스)가 있으면
            rear = (rear+1)%oven_size
            oven[rear] = last
            last += 1   # 치즈가 0으롤 초기화된 경우, 투입될 피자(인덱스)
    print(f'#{tc} {tmp+1}')     # 인덱스 -> 피자 번호

