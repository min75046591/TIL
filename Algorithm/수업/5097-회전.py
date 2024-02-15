"""
N개의 숫자로 이루어진 수열
M = 맨 앞의 숫자를 맨 뒤로 보내는 작업 수
수열의 맨 앞에 있는 숫자를 출력
"""

# rear 가 M일때 그 값을 출력
# M 만큼의 칸을 생성
# 수열을 Q에 각 자리에 하나씩 M만큼 넣음
# 마지막 인덱스의 값 추출

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = [0] * N
    rear = -1

    for i in range(M):
        num = arr[(i+1) % N]  # arr을 M만큼 순회하며 나눈 나머지를 q에 넣는다
        rear = (rear + 1) % N
        q[rear] = num

    print(f'#{tc} {q[rear]}')

# 다른 방법
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'#{tc} {arr[M%N]}')