"""
조건 하에서 사재기를 하여 최대한 이득을 얻자
1. 연속된 N일 동안 물건의 매매가를 예측하여 알 수 있따
2. 하루에 최대 1만큼 구입 가능
3. 판매는 얼마든지 할 수 있음

ex) 3일동안의 매매가가 1, 2, 3이라면 처음 두날에 원료를 구매해서 마지막 날에 팔면
총 3의 이익을 얻을 수 있음

1 1 4 1 3 = 8
1 1 3 1 4 =
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    earn = 0    # 내가 번 돈
    max_price = 0   # 현재 판매가격(최댓값)

    for i in arr[::-1]:     # 뒤에서부터 조사
        if i >= max_price:  # 현재 값이 최대값보다 크거나 같으면
            max_price = i
        else:
            earn += max_price - i
    print(f'#{tc} {earn}')



