N, S = map(int, input().split()) # N:정수의 개수 / S:목표 정수값
nums = list(map(int, input().split()))
result = 0

for i in range(1<<N): # N만큼의 경우의 수
    tmp_li = []
    for j in range(N):
        if i & (1<<j):
            tmp_li += [nums[j]]
    
    if sum(tmp_li) == S:
        result += 1

print(result)