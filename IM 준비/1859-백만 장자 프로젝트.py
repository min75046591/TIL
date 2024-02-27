"""
조건 하에서 사재기를 하여 최대한 이득을 얻자
1. 연속된 N일 동안 물건의 매매가를 예측하여 알 수 있따
2. 하루에 최대 1만큼 구입 가능
3. 판매는 얼마든지 할 수 있음

ex) 3일동안의 매매가가 1, 2, 3이라면 처음 두날에 원료를 구매해서 마지막 날에 팔면
총 3의 이익을 얻을 수 있음
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]
    wallet = []     # 구매한 주식을 저장
    earn = 0        # 이득 본 금액
    week_max = 0    # 주식을 산 이후로 가장 금액이 높을 때

    for i in range(N):
        if arr[i] <= arr[i+1]:
            wallet.append(arr[i])   # 지갑에 산 주식 넣기
        elif arr[i] > arr[i+1]:     # 다음날 가격이 오늘 가격보다 낮을 때
            for j in range(i, N):   # 오늘 가격부터 그 이후 가격중 가장 높을 때 팔기 위해
                if week_max < arr[j]:   # 가장 높은 가격 구하기
                    week_max = arr[j]

            for k in wallet:
                earn += week_max - k    # 가장 높은 가격에서 지갑에 넣어둔 주식 매도

            wallet = []     # 매각 했으니 지갑 초기화
            week_max = 0    # 주식을 판 날 이후로 또 계산하기 위해 초기화

    print(f'#{tc} {earn}')