T = 10
for tc in range(1, T+1):
    N = int(input())    # N 건물의 개수 / 가로 길이
    high = list(map(int, input().split()))    # high 건물의 높이
    # 맨 왼쪽과 오른쪽 두칸은 건물 x
    # 각 빌딩의 최대 높이는 255
    # i를 기준으로 i가 가장 높을 때 두번째로 높은 건물의 높이만큼 빼기
    result = 0  # 조망권 확보된 가구 수 
    for i in range(2, N-2):
        max_high = 0
        for j in range(i-2, i+2+1):
            if i == j:
                continue
            if max_high < high[j]:   # 앞뒤 두칸중 가장 높은 건물
                max_high = high[j]
        if max_high < high[i]:    # 내 위치의 건물이 가장 높고 주위에 두번째로 높은 건물이 있을때
            result += high[i] - max_high    # 조망권 확보 개수 확인
    print(f'#{tc} {result}')

