"""
왼쪽과 오른쪽으로 창문을 열었을때 양쪽 모두 거리 2이상의 공간이 확보될 때
조망권이 확보

조망권이 확보된 세대의 수 반환

맨 왼쪽과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다
"""
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        # 내 건물이 주위 2칸 이내의 건물중 가장 크다면 2번째로 큰 건물의 차 구하기
        max_high = 0
        for j in range(i-2, i+3):
            if i == j:      # 내 위치의 건물은 컨티뉴
                continue
            # 범위중 가장 높은 건물의 값 저장
            if max_high < arr[j]:
                max_high = arr[j]
        # 내 건물의 주위 건물중 가장 높을 때
        if max_high < arr[i]:
            result += arr[i] - max_high
    print(f'#{tc} {result}')