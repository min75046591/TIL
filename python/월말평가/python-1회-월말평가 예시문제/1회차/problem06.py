############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    pass
    # 여기에 코드를 작성합니다.
    # 결과 기본값을 False로 초기화
    result = False
    # user_data1의 'id'의 값을 id_value 변수에 할당
    id_value = user.get('id')
    # id의 마지막 값이 0~9에 있으면 True
    if id_value[-1] in map(str, range(10)):
        result = True
    return result
 

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