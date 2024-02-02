T = int(input())
for tc in range(1, T+1):
    prime_num = [2, 3, 5, 7, 11]
    prime = [0] * 5
    N = int(input())
    idx = 0

    for i in prime_num:
        cnt = 0
        while N % i == 0:
            N = N//i
            cnt += 1
        prime[idx] = cnt
        idx += 1

    print(f'#{tc}', *prime)