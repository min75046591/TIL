"""
16진수 1자리는 2진수 4자리
N자리 16진수를 4자리 2진수로 표시
2진수의 앞자리 0도 반드시 출력
"""
T = int(input())
for tc in range(1, T+1):
    hex_bin = {'0': '0000',
               '1': '0001',
               '2': '0010',
               '3': '0011',
               '4': '0100',
               '5': '0101',
               '6': '0110',
               '7': '0111',
               '8': '1000',
               '9': '1001',
               'A': '1010',
               'B': '1011',
               'C': '1100',
               'D': '1101',
               'E': '1110',
               'F': '1111'}
    result = ''                 # result 값 초기화
    N, num = input().split()    # N 자리수, num 16진수
    for i in range(int(N)):
        result += hex_bin.get(num[i])    # result += hex_bin[num[i]]
    print(f'#{tc} {result}')