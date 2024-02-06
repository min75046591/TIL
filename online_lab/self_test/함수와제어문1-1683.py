number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(NAME, AGE, ADDRESS):
    user_info = {'name':NAME, 'age':AGE, 'address':ADDRESS}
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in name:
    print(f'{i}님 환영합니다!')

print(list(map(lambda name, age, address: create_user(name, age, address), name, age, address)))