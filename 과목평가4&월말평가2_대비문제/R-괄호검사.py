"""
괄호가 정상적인 짝을 이룰 경우 1을 출력
else:
    0을 출력
"""
T = int(input())
for tc in range(1, T+1):
    arr = input()
    stack = []
    result = 1
    for i in arr:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')' or i == '}':
            if stack:   # 스택이 비어있지 않다면
                if (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:               # 짝이 안맞다면
                    result = 0
                    break
            else:                   # 닫는 괄호가 나왔는데 스택이 비어있다면
                result = 0
                break

    if stack:       # 마지막에 스택이 비어있지 않으면
        result = 0

    print(f'#{tc} {result}')