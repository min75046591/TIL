"""
꼭지점을 좌표로
좌표로 종이를 자른 후 가장 큰 종이 조각의 넓이를 구하라!

가장 큰 넓이를 어떻게 구할 것인가...

"""
C, R = map(int, input().split())
# [1] 가능한 가로/세로 자르는 위치를 저장 후 정렬
r_list = [0, R]
c_list = [0, C]
N = int(input())
for _ in range(N):
    t, n = map(int, input().split())
    if t == 0:
        r_list.append(n)
    else:
        c_list.append(n)
# 오름차순 정렬
r_list.sort()
c_list.sort()

# [2] 가장 긴 길이 찾기
r_max = 0
for i in range(1, len(r_list)):
    r_max = max(r_max, r_list[i] - r_list[i-1])

c_max = 0
for i in range(1, len(c_list)):
    c_max = max(c_max, c_list[i] - c_list[i-1])

print(r_max * c_max)


