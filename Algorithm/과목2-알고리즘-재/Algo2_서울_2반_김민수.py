"""
김싸피가 얻을 수 있는 총 점수
N개의 정수
숫자가 적힌 칸 위에서 튕기면 그 숫자만큼의 점수

0번에서 시작
튕기는 거리는 N씩 증가, 총 N번
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    score = 0                       # 점수 초기화
    for i in range(N):              # 게임 횟수
        for j in range(0, N, N-i):  # 튕기는 횟수를 N-i만큼 설정 = 건너뛰는 범위
            score += arr[j]         # 점수에 공이 맞은 위치의 값 더하기

    if score < 0:   # 획득 점수가 0점 이하인 경우
        score = 0   # 점수는 0
    print(f'#{tc} {score}')