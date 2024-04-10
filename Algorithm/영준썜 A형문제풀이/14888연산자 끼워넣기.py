def f(n, k, r):
    global minV, maxV
    if n==k:
        if maxV<r:
            maxV = r
        if minV>r:
            minV = r
    else:
        if op[0]>0:
            op[0] -= 1
            f(n+1, k, r+card[n])
            op[0] += 1
        if op[1]>0:
            op[1] -= 1
            f(n+1, k, r-card[n])
            op[1] += 1
        if op[2]>0:
            op[2] -= 1
            f(n+1, k, r*card[n])
            op[2] += 1
        if op[3]>0:
            op[3] -= 1
            if r//card[n]<0:
                d = -(abs(r)//abs(card[n]))
            else:
                d = r//card[n]

            f(n+1, k, d)
            op[3] += 1


N = int(input())
card = list(map(int, input().split()))
op = list(map(int, input().split()))

minV = 10000000000
maxV = -10000000000
f(1, N, card[0])
print(maxV)
print(minV)