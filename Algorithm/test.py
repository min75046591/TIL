# path = []   # 경로 출력용
#
# def KFC(x):
#     if x == 3:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x + 1)
#         path.pop()
#
# KFC(0)

path = []
used = [False, False, False]
N = 0

def type1(x):
    if x == N:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        type1(x + 1)
        path.pop()

def type2(x):
    if x == 2:
        print(path)
        return

    for i in range(1, 7):
        if used[i] == True : continue
        used[i] = True
        path.append(i)
        type2(x + 1)
        path.pop()
        used[i] = False

used = [False for _ in range(7)]
N, type = map(int, input().split())

if type == 1:
    type1(0)

if type == 2:
    type2(0)