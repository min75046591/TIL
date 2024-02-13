T = int(input())
for tc in range(1, T+1):
    stack = []
    fx = list(input().split())
    for i in fx:
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
            if len(stack) == 1:
                print(f'#{tc} {int(stack.pop())}')
            else:
                print(f'#{tc} error')
                break
# 상무형 코드 한번 보기
T = int(input())
for tc in range(1, T+1):
    stack = []
