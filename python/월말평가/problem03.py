############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def check_user_id(user):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # user_id_check 변수에 'user_id'키의 값을 할당
    user_id_check = user.get('user_id')
    
    # 딕셔너리에서 가져온 값의 길이를 재기 위해 for문으로 길이 확인
    id_len_count = 0
    for _ in user_id_check:
        id_len_count += 1
    

    # id_len_count. 즉, user_id 키 값의 길이가 4이상 16미만인지 확인
    # 범위 안에 들어간다면 True 반환. 그 외에는 False 반환
    if 4 <= id_len_count < 16:
        return True
    else:
        return False


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(check_user_id(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_user_id(user_data2))  # False
#####################################################
