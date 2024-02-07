T = int(input())
for tc in range(1, T+1):
    a = input()
    stack = []      # 여는 괄호를 저장하기 위한 스택
    result = 0      # 초기 결과 값은 0으로 설정

    for i in a:
        if i == '{' or i == '(':  # 여는 괄호인 경우 스택에 push
            stack.append(i)
        elif i == '}' or i == ')': # 닫는 괄호인 경우
            if stack != []:  # 스택이 비어있지 않으면
                # 짝이 있는 괄호를 스택에서 제거
                if (i == '}' and stack[-1] == '{') or (i == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    break  # 짝이 안 맞으면 루프 종료
            else:
                break

    else:
        if stack == []:  # 스택이 비어있으면
            result = 1  # 결과를 1으로 설정

    print(f'#{tc} {result}')

    

'''
op = {')':'(', '}':'{'}
T = int(input())
for tc in range(1, T+1):
    s = input()
    ans = 1
    stack = []

    for x in a:
        if x in '{}()':     # 괄호인 경우
            if x in '{(':    # 여는 괄호면 push()
                stack.append((x))
            else:    # 닫는 괄호면 
                if not stack:   # (1) 스택이 비어있으면 오류(break)
                    ans = 0
                    break
                else:           # 스택에 여는 괄호가 있으면
                    t = stack.pop()
                    if t != op[x]:  # (2) pop()해서 짝이 맞지 않으면 오류
                        ans = 0
                        break
                
                # (3) 짝이 맞으면 계속
        else: # 주어진 입력에 대한 확인이 끝난 경우
            if stack:
                ans = 0
        print(f'#{tc} {ans}')    # (4) 스택이 비어있지 않으면(여는 괄호) 오류 ans = 0
    '''        

            

# 괄호가 )( 이렇게 있으면 정상적인 짝이 아니기 때문에 이 코드는 testcase 통과 못함
'''
T = int(input())
for tc in range(1, T+1):
    a = list(input())
    N = len(a)
    b = 0 # 왼쪽 괄호
    c = 0 # 오른쪽 괄호
    
    for i in a:
        if i == '{' or i == '(':
            b += 1
        
        elif i == '}' or i == ')':
            c += 1
        
    result = b - c
    if result == 0:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} 0')
'''