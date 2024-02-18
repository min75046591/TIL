"""
8개의 숫자 입력 받음
첫번째 숫자 1 감소하고 맨 뒤로 보냄
그 다음 숫자는 i+1씩 감소
숫자가 0보다 작아지면 0으로 유지되며(맨 마지막은 항상 0), 종료
"""
for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    while arr[7] != 0:
        for i in range(5):  # 5번 감소가 1 사이클
            num = arr.pop(0)
            num -= (i+1)
            if num <= 0:  # 감소한 숫자가 0 이하면 0으로 저장
                num = 0
            arr.append(num)
            if arr[7] == 0:
                break

    print(f'#{tc}', *arr)