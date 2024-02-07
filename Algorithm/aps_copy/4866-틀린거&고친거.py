# 런타임 에러와 테스트케이스 19개중 6개 맞음
T = int(input())
for tc in range(1, T+1):
    a = list(input())
    stack = []      # 여는 괄호를 저장하기 위한 스택
    result = 1      # 초기 결과 값은 1로 설정

    for i in a:
        if i == '{' or i == '(':  # 여는 괄호인 경우 스택에 push
            stack.append(i)
        elif i == '}' or i == ')': # 닫는 괄호인 경우
            # 짝이 있는 괄호를 스택에서 제거
            if (i == '}' and stack[-1] == '{') or (i == ')' and stack[-1] == '('):
                stack.pop()
            else:
                break  # 짝이 안 맞으면 루프 종료
    else:
        if stack:  # 스택이 비어있지 않으면
            result = 0  # 결과를 0으로 설정

    print(f'#{tc} {result}')


# 지피티로 고친거
T = int(input())
for tc in range(1, T+1):
    a = input()
    stack = []      # 여는 괄호를 저장하기 위한 스택
    result = 1      # 초기 결과 값은 1로 설정

    for i in a:
        if i == '{' or i == '(':  # 여는 괄호인 경우 스택에 push
            stack.append(i)
        elif i == '}' or i == ')': # 닫는 괄호인 경우
            if stack != []:  # 스택이 비어있지 않으면
                # 짝이 있는 괄호를 스택에서 제거
                if (i == '}' and stack[-1] == '{') or (i == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    result = 0  # 짝이 안 맞으면 결과를 0으로 설정
                    break  # 루프 종료
            else:
                result = 0  # 스택이 비어있는데 닫는 괄호가 나오면 결과를 0으로 설정
                break

    else:
        if stack:  # 스택이 비어있지 않으면
            result = 0  # 결과를 0으로 설정

    print(f'#{tc} {result}')