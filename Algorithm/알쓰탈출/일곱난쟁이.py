'''
일곱 난쟁이의 키의 합이 100
'''
cm = [int(input()) for _ in range(9)]
N = 9
cm.sort()

for i in range(1<<N):
    tmp_sum = 0
    real = []
    
    for j in range(N):
        if i & (1<<j):
            tmp_sum += cm[j]
            real.append(cm[j])
    
    if tmp_sum == 100 and len(real) == 7:
        break

for result in real:
    print(result)