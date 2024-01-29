T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    b = int(input())
    c = list(map(int, input().split()))
    max_val = c[0]
    min_val = c[0]

    for i in c:
        if i > max_val:
            max_val = i

        if i < min_val:
            min_val = i

    
    print(f'#{_} {max_val - min_val}')
