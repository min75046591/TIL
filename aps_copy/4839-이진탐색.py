def binary_search(page, target):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        c = int((start + end) / 2)
        if c == target:
            break
        elif c > target:
            end = c - 1
        else:
            start = c + 1
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split())  # 전체 쪽 수:P, A, B가 찾을 쪽 번호
    cnt_a = binary_search(p, pa)
    cnt_b = binary_search(p, pb)

    if cnt_a < cnt_b:
        print(f'#{tc} A')
    elif cnt_a > cnt_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')