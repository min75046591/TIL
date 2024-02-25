# import sys
# # 표준 입력 파일을 읽기로 설정
# sys.stdin = open('input_view.txt', 'r')

# 입력값 받기
T = 10
for tc in range(1, T+1):
    N = int(input())  # 건물 개수
    high = list(map(int, input().split()))  # N개의 건물 높이
    result = 0
    for i in range(2, N-2): # 앞에 2칸이 땅이라 2부터 시작. 
        max_high = 0
        for j in range(i-2, i+2+1):
            if i == j:
                continue
            if max_high < high[j]:    # 범위중 가장 높은 건물의 값을 저장
                max_high = high[j]
        if max_high < high[i]:  # 현재 건물이 주변건물들 보다 높을 때
            result += high[i] - max_high    # 조망권 개수 확인
    print(f'#{tc} {result}')