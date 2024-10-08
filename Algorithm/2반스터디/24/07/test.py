# 올바르지 못한 괄호열이면 0을 출력
# 큰 틀에서 안 쪽 부터 계산
'''
() = 2
[] = 3
중첩 괄호는 *
개별 괄호는 +
'''
### 틀림

str = list(input())
stack = []
answer = 0

for i in range((len(str))):
    if str[i] == '(':
        if str[i+1] == ']':
            answer = 0
            break
        else:
            stack.append('(')
            pass
    elif str[i] == ')':
        if stack and stack[-1] == '(':
            if len(stack) > 1:
                answer *= 2
                stack.pop()
            elif len(stack) == 1:
                answer += 2
                stack.pop()


    elif str[i] == '[':
        if str[i+1] == ')':
            answer = 0
            break
        else:
            stack.append('[')
            pass
    elif str[i] == ']':
        if stack and stack[-1] == '[':
            if len(stack) > 1:
                answer *= 3
                stack.pop()
            elif len(stack) == 1:
                answer += 3
                stack.pop()
print(answer)



### 정답

str = input().strip()
stack = []
temp = 1
answer = 0

for i in range(len(str)):
    if str[i] == '(':
        stack.append('(')
        temp *= 2
    elif str[i] == '[':
        stack.append('[')
        temp *= 3
    elif str[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if str[i-1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    elif str[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if str[i-1] == '[':
            answer += temp
        stack.pop()
        temp //= 3

# 남아있는 괄호가 있으면 0으로 설정
if stack:
    answer = 0

print(answer)
