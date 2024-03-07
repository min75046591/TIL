T = int(input())
for tc in range(1, T+1):
    arr = input()
    result = 1
    stack = []

    for i in arr:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == ')' or i == '}':
            if stack:
                if (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{'):
                    stack.pop()
                else:           # 다른 괄호가 들어있을때
                    result = 0
                    break
            else:               # 스택이 비어있으면 안됌
                result = 0
                break
    if stack:           # 괄호가 스택에 남아있으면 안됌
        result = 0

    print(f'#{tc} {result}')