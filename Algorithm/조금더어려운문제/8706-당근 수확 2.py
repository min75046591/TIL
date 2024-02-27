"""
수레로 당근을 옮기기.
수확한 당근을 모으는 통과 수레 보관 장소가 0번 구역
0번에서 출발해 가까운 순서로 당근을 수레에 싣다가 수레가 꽉 차면 0번으로 돌아와
수레를 비우고, 다시 당근을 실으러 이동함

모든 당근을 0번 구역으로 옮기기 까지 일꾼이 이동한 총 거리를 계산
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # M 수레에 실을 수 있는 양
    arr = [0] + list(map(int, input().split()))
    total = 0   # 누적 거리
    cart = 0    # 수레에 남은 양

    for i in range(1, N+1):
        cnt = (arr[i]+cart) // M
        cart = (arr[i]+cart) % M
        total += cnt * i

    if cart > 0:
        total += N

    result = total * 2
    print(f'#{tc} {result}')