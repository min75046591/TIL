"""
반복 문자를 지운 후 남은 문자열의 길이를 출력하시오.
남은 문자열이 없으면 0을 출력
"""
# 연속되는 문자를 없애기
T = int(input())
for tc in range(1, T+1):
    arr = input()
    stack = []
    for i in arr:
        if stack:           # 스택이 비어있지 않다면
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f'#{tc} {len(stack)}')