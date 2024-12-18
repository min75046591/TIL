from collections import deque

def hex_to_decimal(hex_str):
    return int(hex_str, 16)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(input().strip())
    n = N // 4
    num = deque(nums)
    result_set = set()

    # 회전 및 고유 숫자 수집
    for _ in range(n):
        # deque를 회전하여 새로운 조합 생성
        for i in range(0, N, n):
            # 현재 회전된 시퀀스 추출
            current_number = ''.join(list(num)[i:i+n])
            result_set.add(current_number)

        # deque를 우측으로 회전
        num.rotate(1)

    # 16진수 문자열을 10진수 숫자로 변환
    decimal_numbers = [hex_to_decimal(num_str) for num_str in result_set]

    # 10진수 숫자를 내림차순으로 정렬
    sorted_decimals = sorted(decimal_numbers, reverse=True)

    # K번째로 큰 숫자 찾기 (1부터 시작하는 인덱스로 고려)
    if 1 <= K <= len(sorted_decimals):
        answer = sorted_decimals[K - 1]
    else:
        answer = None  # K가 범위를 벗어나는 경우 처리

    print(f"#{tc} {answer}")