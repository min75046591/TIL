

# print(person['name'])
# print(person.get('name'))
# print(person.get('country'))
# print(person.get('country', '키가 없습니다.'))

# print(person.keys())  # dict_keys(['name', 'age'])

# for key in person.keys():
#     print(key)

# print(person.values())  # dict_values(['Alice', 25])

# for value in person.values():
#     print(value)

# print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

# for key, value in person.items():
#     print(key, value)

# print(person.pop('age'))
# print(person)
# print(person.pop('country', None))

# print(person.setdefault('country', 'KOREA'))  # KOREA
# print(person)  # {'name': 'Alice', 'country': 'KOREA'}

# person.clear()
# print(person)
person = {
    'name': 'Alice', 
    'age': 25
}

other_person = {
    'name': 'Jane',
    'gender': 'Female'
}

person.update(other_person)
print(person)

person.update(age=50, country='KOREA')
print(person)

list = [
    {'john': '521-1234'},
    {'Lisa': '521-8976'},
    {'Sandra': '521-9655'}
]
dict = {
    'john': '521-1234',
    'Lisa': '521-8976',
    'Sandra': '521-9655'
}

dict.get('Lisa')