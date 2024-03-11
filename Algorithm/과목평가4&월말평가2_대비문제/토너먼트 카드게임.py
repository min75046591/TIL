"""
문자열 연산자가 이번엔 '+' 와 '*' 두 종류
"""
def win(a,b):
    # 가위1 바위2 보3  2>1, 3>2, 1>3
    if card[b]-card[a]==1 or card[b]-card[a] == -2:  # 승자 b
        return b
    else:
        return a

def f(i, j):    # i~j번 사이 승자를 리턴하는 함수
    if i==j:    # 한명인 경우 부전승
        return i
    else:
        left = f(i, (i+j)//2)
        right = f((i+j)//2+1, j)
        return win(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc} {f(0, N-1)+1}')