'''
가장 많은 카드의 숫자와 장 수 구하기
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 카드 장 수
    arr = list(map(int, input()))
    counts = [0] * 10   # 0~9 까지 각 숫자의 등장 횟수를 저장하기 위한 리스트를 초기화
    # 카드의 장 수만큼 반복하여 각 숫자의 등장 횟수를 counts 리스트에 기록
    for i in range(N):
        counts[arr[i]] += 1

    max_count = counts[0]  # 가장 많은 카드의 장 수를 초기화
    max_num = 0 # 가장 많은 카드의 숫자를 초기화

    for j in range(10):
        if max_count <= counts[j]:  # 현재 숫자에 대한 카운트가 최대값보다 크거나 같으면 업데이트
            max_count = counts[j]
            max_num = j # 가장 많은 카드의 숫자를 현재 숫자로 업데이트

    print(f'#{tc} {max_num} {max_count}')