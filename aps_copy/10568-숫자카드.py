# 입력값 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    counts = [0] * 10
    # 숫자 개수
    for i in range(N):
        counts[arr[i]] += 1

    max_count = counts[0]
    max_num = 0

    for j in range(10):
        if max_count <= counts[j]:
            max_count = counts[j]
            max_num = j

    print(f'#{tc} {max_num} {max_count}')
