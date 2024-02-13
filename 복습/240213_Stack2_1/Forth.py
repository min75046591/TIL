T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    for i in arr:
        if i.isdigit():
            stack.append(int(i))
        elif i in '+-*/':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b+a)
                if i == '-':
                    stack.append(b-a)
                if i == '*':
                    stack.append(b*a)
                if i == '/':
                    stack.append(b/a)
            elif len(stack) < 2:
                print(f'#{tc} error')
                break
        elif i == '.':
            if len(stack) == 1:  # 스택이 1개만 존재 = 연산이 끝난 결과값 1개
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
                break
