"""
실내공조 제어 시스템은 승객이 탑승 중일 때 항상
t1 ~ t2 실내 온도를 유지할 수 있도록 함.
현재(0분) 실내온도는 실외온도와 같다.
실내공조 제어 시스템은 실내온도를 조절하기 위해 에어컨의 전원을 켜 희망온도를 설정
희망온도는 에어컨의 전원이 켜져 있는 동안 원하는 값으로 변경할 수 있음

"""

# 20개중 3개 맞음

def solution(temperature, t1, t2, a, b, onboard):
    # 현재 온도를 나타내는 변수
    current_temp = temperature
    # 현재 시점에서 최소 소비전력을 나타내는 변수
    total_power = 0
    # 에어컨의 상태를 나타내는 변수 (True: 켜짐, False: 꺼짐)
    ac_on = False
    # 희망 온도를 나타내는 변수
    target_temp = None

    for i in range(len(onboard)):
        if onboard[i] == 1:  # 승객이 탑승 중인 시간
            if not ac_on:  # 에어컨이 꺼져 있으면 켬
                ac_on = True
                # 희망온도를 쾌적한 범위의 중앙값으로 설정
                target_temp = (t1 + t2) // 2
            
            # 현재 온도가 쾌적한 범위 안에 있지 않으면 에어컨을 이용하여 맞춤
            if current_temp < t1:
                total_power += a
                current_temp += 1
            elif current_temp > t2:
                total_power += a
                current_temp -= 1
            else:
                total_power += b
        else:  # 승객이 탑승 중이 아닌 시간
            if ac_on:  # 에어컨이 켜져 있으면 끔
                ac_on = False
            
            # 현재 온도가 실외온도로 1도 변화
            if current_temp < temperature:
                current_temp += 1
            elif current_temp > temperature:
                current_temp -= 1

    return total_power