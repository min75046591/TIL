# for i in range(5):
#     a, b = map(int, input().split())
#     print(a+b)

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break