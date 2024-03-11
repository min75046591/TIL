"""
변이 1인 정사각형 n개를 가지고 있다.
이 정사각형을 이용해서 만들 수 있는 직사각형의 개수

두 직사각형 A, B가 있을때, A를 이동, 회전 시켜서 B를 만들 수 없으면
두 직사각형은 다르다고 한다.

"""
N = int(input())
ans = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        if i*j <= N:
            ans += 1
print(ans)