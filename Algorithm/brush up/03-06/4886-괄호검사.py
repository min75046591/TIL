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
                else:
                    result = 0
                    break
            else:
                result = 0
                break
    if stack:
        result = 0

    print(f'#{tc} {result}')