"""
문자열로 이루어진 계산식.
후위 표기식으로 바꾸어 계산하는 프로그램
"""

T = 10
for tc in range(1, T+1):
    N = int(input()) # 문자열 길이
    sum_list = list(input())
    # 숫자와 연산기호 따로 담기
    num_li = []
    cal_li = []
    for i in sum_list:
        if i == '+':
            cal_li.append(i)
        else:
            num_li.append(i)
    result_li = num_li + cal_li
    stack = []
    for i in result_li:
        if i.isdigit():     # 현재 문자가 숫자라면 스택에 추가
            stack.append(i)
        else:               # 연산기호일 경우, 스택에서 두개의 숫자를 꺼내와 정수로 변환
            num_1 = int(stack.pop())
            num_2 = int(stack.pop())
            stack.append(num_2 + num_1)
    print(f'#{tc} {stack.pop()}')

