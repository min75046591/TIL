"""
연습문제 1
스택을 구현
구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고
다시 3번 꺼내서 출력
"""
def push(n):
    global top
    top += 1
    if top == N:
        print('overflow')
    else:
        stack[top] = n

# top 초기화, stack 설정
top = -1
N = 10
stack = [0] * N

top += 1
stack[top] = 10     # top 1 증가하면서 스택에 10 넣기 == stack[0] = 10

top += 1
stack[top] = 20     # top 1 증가하면서 스택에 20 넣기 == stack[1] = 20

push(30)

while top >= 0:
    top -= 1
    print(stack[top+1])