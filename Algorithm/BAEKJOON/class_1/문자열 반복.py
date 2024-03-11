"""
문자열 S를 입력받고
각 문자를 R번 반복해 새 문자열 P를 만든 후 출력

"""
T = int(input())
for tc in range(1, T+1):
    R, S = list(input().split())
    new_s = ''
    for i in S:
        new_s += i * int(R)

    print(new_s)