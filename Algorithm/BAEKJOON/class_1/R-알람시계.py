"""
45분 일찍 알람 설정하기
원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸기

24시간 표현을 사용 -> 0:0 ~ 23:59
시간을 나타낼 때 불필요한 0은 사용하지 않는다
"""
H, M = map(int, input().split())    # H시 M분
# sum_time = 60*H + M - 45
# new_H = sum_time//60
# new_M = sum_time % 60

if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60
print(H, M-45)