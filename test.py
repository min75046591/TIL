N = int(input())

for i in range(N):
    tmp = i
    for s in str(i):
        tmp += int(s)    

    ##print(tmp)/

    if tmp == N:
        print(i)
        break
    elif i == N:
        print(0)
