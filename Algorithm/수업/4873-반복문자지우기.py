# push or append를 통해 문자를 stack에 담는다
# 조사를 하면서 시작하는 문자와 그 다음의 문자가 같고 개수가 2이상이면
# pop으로 삭제한다.

T = int(input())
for tc in range(1, T+1):
    txt = list(input())
    stack = []
    for i in txt:
        if len(stack) == 0:      # 스택이 비어있다면 스택에 요소를 추가
            stack.append(i)
        else:
            if i == stack[-1]:   # 들어간 요소 i와 stack의 마지막 원소가 같으면 삭제
                stack.pop()
            else:
                stack.append(i)  # 같지 않다면 i를 stack에 넣기
    print(f'#{tc} {len(stack)}')