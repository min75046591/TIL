############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    # id를 키로하는 값을 user_value에 할당
    user_value = user.get('id')
    # if문으로 user_value의 마지막 인덱스에 해당하는 글자가
    # 0~9인지 확인. 숫자로 있으면 True 반환. 없으면 False 반환.
    if user_value[-1] in map(str, range(10)):
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