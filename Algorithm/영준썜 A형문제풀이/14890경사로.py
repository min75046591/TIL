def f(a, N, L): # 리스트 a 검사
    d = a[0]
    cnt = 1
    v = []
    c = []
    for i in range(1, N):
        if d==a[i]:
            cnt +=1
        else:
            v.append(d)
            c.append(cnt)
            d = a[i]
            cnt = 1
    v.append(d)
    c.append(cnt)
    for i in range(1, len(v)):
        diff = v[i] - v[i-1]
        if diff == 1: # 높이 1증가
            if c[i-1]<L: # 오르막을 만들 수 없으면
                return 0
            else:
                c[i-1] -= L
        elif diff == -1: # 높이 1감소
            if c[i]<L:
                return 0
            else:
                c[i] -= L
        else:
            return 0
    return 1

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans += f(arr[i], N, L)
    a = []
    for j in range(N):
        a.append(arr[j][i])
    ans += f(a, N, L)
print(ans)