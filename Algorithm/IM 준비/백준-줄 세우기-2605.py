N = int(input())    # 학생 수
arr = list(map(int, input().split()))
tmp = []
for i in range(1, N+1):
    tmp.insert(arr[i-1], i)
print(*reversed(tmp))