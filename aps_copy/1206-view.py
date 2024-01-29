import sys
# 표준 입력 파일을 읽기로 설정
sys.stdin = open('input_view.txt', 'r')

# 입력값 받기
T = 10
for tc in range(1, T+1):
    N = int(input())  # 건물 개수
    high = list(map(input().split()))  # N개의 건물 높이

    for i in range(2, N-3): # 앞에 2칸이 땅이라 2부터 시작. 
                            # 뒤에 -3은 굳이 끝까지 갈 필요 없기 때문

    