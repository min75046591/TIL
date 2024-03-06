"""
연습문제 2
괄호의 짝을 검사하는 프로그램을 작성

input
()()((()))
((()((((()()((()())((())))))
"""
arr = input()
stack = []
for i in arr:
    if i == '(':
        stack.append(i)
    if i == ')':
        if stack:
            stack.pop()

if stack:
    ans = 'False'

else:
    ans = 'True'
print(ans)

