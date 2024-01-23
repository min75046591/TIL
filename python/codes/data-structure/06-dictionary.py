# person = {
#     'name':'Alice', 
#     'age':25
# }

# print(person['name'])   # 둘 다 키와 연결된 값을 반환하지만
# print(person.get('name')) # 없는 키를 호출했을때 결과가 다름
# print(person.get('country'))
# print(person.get('country', '키가 없습니다.'))

# print(person.keys())  # dict_keys(['name', 'age'])
# # ['name', 'age'] -> 1. key들의 모임  2. 반복 가능

# for key in person.keys():
#     print(key)


# print(person.values())  # dict_values(['Alice', 25])

# for value in person.values():
#     print(value)


# print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
# # 튜플로 묶여있어 쌍으로 나옴을 알 수 있음

# for key, value in person.items():  # 언패킹이 됨
#     print(key, value)


# # print(person.pop('age'))
# print(person)
# # print(person.pop('country'))  # KeyError: 'country'
# print(person.pop('country', None)) # 디폴트 값인 None이 나옴


# print(person.setdefault('country', 'KOREA'))  # KOREA
# print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# other_person = {
#     'name':'Jane',
#     'gender':'Female'
# }

# person.update(other_person) # {'name': 'Jane', 'age': 25, 'country': 'KOREA', 'gender': 'Female'}
# # Alice가 사라짐. 마지막에 추가한 내용이 업데이트
# print(person)

# person.update(age=50)  # age가 50으로 바뀜. 간단하게 값을 추가할때 유용함
# print(person)

# person.clear()
# print(person)


# list = [
#     {'john':'521-1234'}
#     {'Lisa':'521-8976'}
#     {'Sandra':'521-9655'}

# ]
# list는 위에서 부터 확인하며 내려오기 때문에 길이가 길어질수록
# 검색의 시간이 매우 늘어남.
# But 딕셔너리는 바로 찾을 수 있음. 해시 테이블 원리로 인해!
# 순서가 상관이 없는 set와 dict

# dict = {
#     'john':'521-1234',
#     'Lisa':'521-8976',
#     'Sandra':'521-9655'
# }


my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
my_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

print(hash(1))
print(hash(1))
print(hash('a'))
print(hash('a'))