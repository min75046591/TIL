K = 3
N = 6
arr = [0, 1, 0, 1, 1, 1]
ans = 0
cnt = 0
# 가로 K만 가능. 세로는 불가능
for i in range(N):
    if arr[i] == 0:
        if cnt == K:  # 0 만나기 전에 1이 K개 있었는지 확인
            ans += 1
        cnt = 0
    else:   # arr[i] == 1
        cnt += 1
        if i==N-1:
            if cnt == K:
                ans += 1
print(ans)