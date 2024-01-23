n, k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for coin in coins:
    if coin <= k:
        cnt += k // coin
        k -= (k // coin) * coin
print(cnt)