def is_id_valid(user):
    pass
    # 여기에 코드를 작성합니다.
    result = False
    id_value = user.get('id')
    if id_value[-1] in map(str, range(10)):
        result = True
    return result
 
    

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
