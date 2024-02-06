############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # password의 키 값을 user_password에 할당
    user_password = user.get('password')
    # pw_confirm에 password_confirm 키 값을 할당
    pw_confirm = user.get('password_confirm')
    # 길이를 재기 위해 password_len 변수에 문자열이 들어갈 때 마다 +1
    password_len = 0

    # password 길이 재기
    for _ in user_password:
        password_len += 1
    
    # 만약 password 길이가 8이상 32미만이면서, password의 값과 password_confirm의 값이 같을 때
    # True 반환. 그 외는 False 반환 
    if 8 <= password_len < 32 and pw_confirm == user_password:
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
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
