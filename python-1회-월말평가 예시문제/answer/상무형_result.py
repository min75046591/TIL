############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 max() 사용 시 감점
def max_score(score_list):
    best_score = 0

    for score in score_list:
        if score > best_score:
           best_score = score
    
    return best_score
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(max_score(scores1)) # 90
#####################################################

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def over(ssafy_result):
    count = 0
    for i, v in enumerate(ssafy_result):
        if v >= 60:
            count += 1

    return count

    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(over(scores1)) # 3
#####################################################

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count() 를 사용시 감점
def menu_count(restorant_dict):
    menu_num = 0
    for i in restorant_dict['menus']:
        menu_num += 1

    return menu_num
    # 여기에 코드를 작성합니다.
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
restorant1 = {
    "id": 11,
    "user_rating": 5.5,
    "name": "김밥나라",
    "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
    "location": "서울특별시 강남구 역삼동 123-123"
}
print(menu_count(restorant1)) # 4
#####################################################

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def turn(temperature_list):
    max_temp = []
    min_temp = []
    new_menu = {}
    for i in temperature_list:
        max_temp += [i[0]]
        min_temp += [i[1]]
    new_menu['maximum'] = max_temp
    new_menu['minimum'] = min_temp
    
    return new_menu
    # 여기에 코드를 작성합니다.


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

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user):
    if user['id'] and user['password']:
        return True
    else:
        return False
    
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 

user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    if str.isdigit(user['id'][-1]) == True:
        return True
    else:
        return False 
    pass
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################