# 첫 줄
number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1

print(f'현재 가입 된 유저 수 : {number_of_people}')

# 두 번째 줄
def create_user(name, age, address):
    user_info = {'name':"", "age":0, "address":""}
    user_info['name'] = name
    user_info["age"] = age
    user_info["address"] = address
    print(f'{name}님 환영합니다!')
    return user_info

# 세 번째
result = create_user('홍길동', 30, '서울')
print(result)

# 네 번째
increase_user()
print(f'현재 가입 된 유저 수 : {number_of_people}')