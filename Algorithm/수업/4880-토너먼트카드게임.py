"""
인원수 : 1~N
전체를 두 개의 그룹으로 나누기
그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자
-> 여기서 잠깐!!
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠서 뽑음
총 4그룹
그룹을 나눌땐 왼쪽은 (i+j)//2 오른쪽은 (i+j)//2+1

1 : 가위
2 : 바위
3 : 보
if 카드번호가 같으면 번호가 작은 쪽이 승!

N명의 학생들이 카드를 골랐을 때 1등을 찾아라
"""
def win(a, b):
    # 가위1 바위2 보3 2>1, 3>2, 1>3
    if card[b]-card[a] == 1 or card[b]-card[a] == -2:  # 승자 b
        return b
    else:
        return a
    
def f(i, j):    # i~j번 사이 승자를 리턴하는 함수
    if i==j:    # 한명인 경우 부전승
        return 1
    else:
        left = f(i, (i+j) // 2)
        right = f((i+j) // 2+1, j)
        return win(left, right)
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 학생수, 1~N번까지
    card = list(map(int, input().split()))
    print(f'#{tc} {f(0, N-1)+1}')