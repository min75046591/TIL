# 1816

"""
3
1000036000099
1500035500153
20000000000002
"""

N = int(input())
for _ in range(N):
    number = int(input())

    # 풀이 로직
    for i in range(2, 1_000_001):
        if number % i == 0: # 100만 이하의 약수가 존재한다
            print("NO")
            break

        if i == 1_000_000:  # 백만까지 도달했는데 멈추지 않았다면 100만 이하의 약수가 없다
            print("YES")