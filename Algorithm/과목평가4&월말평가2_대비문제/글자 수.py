T = int(input())
for tc in range(1, T+1):
    str_1 = list(input())
    str_2 = list(input())
    max_v = 0
    for i in str_1:
        cnt = 0
        for j in str_2:
            if i == j:
                cnt += 1
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')