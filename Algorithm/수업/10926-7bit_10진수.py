T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    num = input()
    for n in range(0, 70, 7):
        a = num[n:n+7]
        result = 0
        for i in range(7):
            result += int(a[i]) * 2 ** (6-i)
        print(result, end=' ')
    print()