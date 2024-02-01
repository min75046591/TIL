N = int(input())

result = 0
for i in range(N):
    tmp = i
    for s in str(i):
        tmp += int(s)    

    print(tmp)

    if tmp == N:
        print(tmp)
    elif i == N:
        print(0)




# 207 + 2 + 1 + 6 = 216