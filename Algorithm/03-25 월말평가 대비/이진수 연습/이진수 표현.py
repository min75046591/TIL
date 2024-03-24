import sys
sys.stdin = open("input.txt", "r")

# M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 'OFF'

    M = bin(M)
    len_M = len(M)
    cnt = 0
    for i in M[len_M-N:len_M]:
        if i == '1':
            cnt += 1
    if cnt == N:
        result = 'ON'
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {result}')