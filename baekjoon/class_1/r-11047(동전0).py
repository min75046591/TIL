n, k = map(int,input().split())

coin_list = list()
for _ in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse = True)
coin_tmp_cnt = 0

for i in coin_list:
    coin_tmp_cnt += (k // i)
    k = k % i
print(coin_tmp_cnt)