"""
두 개의 문자열중 2문자열 안에 문자열1과 일치하는 부분이 있는지 찾아라
존재하면 1, 없으면 0
"""
T = int(input())
for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    result = 0
    if str_1 in str_2:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')