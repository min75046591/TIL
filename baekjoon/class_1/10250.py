T = int(input())
for test_case in range(T):
    H,W,N = map(int,input().split())
    tmp_h = N%H
    tmp_w = N//H + 1
    if N%H == 0:
        tmp_h = H
        tmp_w -= 1
    if tmp_w < 10:
        tmp_w = '0'+ str(tmp_w)
    print(str(tmp_h)+str(tmp_w))