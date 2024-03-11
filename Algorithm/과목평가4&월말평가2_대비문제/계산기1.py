"""
문자열로 이루어진 계산식을 후위표기식으로 바꾸어 계산
"""
T = 10
for tc in range(1, T+1):
    N = int(input())
    sum_list = list(input())
    # 숫자와 연산기호 따로 담기
    num_li = []
    cal_li = []
    for i in sum_list:
        if i == '+':
            cal_li.append(i)
        else:
            num_li.append(i)

    stack = []
    result_li = num_li + cal_li
    for j in result_li:
        if j.isdigit():  # 숫자인지 확인하는 내장함수
            stack.append(j)
        else:
            num_1 = int(stack.pop())
            num_2 = int(stack.pop())
            stack.append(num_2 + num_1)
    print(f'#{tc} {stack.pop()}')