############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.


def turn(temperature_list):
    # 최대 저소 온도 정보를 저장할 리스트를 만든다.
    maximum = []
    minimum = []
    
    # 반복문을 돌면서 리스트 요소의 첫 번째를 maximum에
    # 요소 두 번째를 minimum에 넣는다.
    for temp_list in temperature_list:
        maximum.append(temp_list[0])
        minimum.append(temp_list[1])
        # 딕셔너리로 반환
        result_dict = {'maximum':maximum, 'minimum':minimum}
    return result_dict
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
temperatures1 = [
    [9, 3],
    [9, 0],
    [11, -3],
    [11, 1],
    [8, -3],
    [7, -3],
    [-4, -12]
]
print(turn(temperatures1)) 
# {'maximum': [9, 9, 11, 11, 8, 7, -4], 'minimum': [3, 0, -3, 1, -3, -3, -12]}
#####################################################