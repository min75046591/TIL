# set 메서드
'''
- s.add(x) : 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
- s.clear() : 세트 s의 모든 항목을 제거
- s.remove(x) : 세트 s에서 항목 x를 제거. x가 없을 경우 Key error
- s.pop() : 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
- s.discard(x) : 세트 s에서 항목 x를 제거 
- s.update(iterable) : 세트 s에 다른 iterable 요소를 추가
'''

# s.add(x) : 세트에 x를 추가
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add(4)
print(my_set) 

my_set.add(4)
print(my_set)

'''
{'a', 2, 3, 'b', 1, 'c', 4}
{'a', 2, 3, 'b', 1, 'c', 4}
'''
# 순서가 정해져 있지 않음. 중복된 요소는 set의 특성으로 하나만 출력됨
print('-----')


# s.clear() : 세트의 모든 항목을 제거
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.clear()
print(my_set) # set()

print('-----')


# s.remove(x) : 세트에서 항목 x를 제거
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.remove(2)
print(my_set) # {'b', 3, 1, 'c', 'a'}

# my_set.remove(10)
# print(my_set) # KeyError

# s.discard() : 세트 s에서 항목 x를 제거. 
#               -> remove 와 달리 에러 없음
my_set = {1, 2, 3}

my_set.discard(2)
print(my_set) # {1, 3}

my_set.discard(10)
print(my_set) # {1, 3} -> 에러가 아닌 그대로 출력

print('-----')


# s.pop() : 세트에서 임의의 요소를 제거하고 반환
# 반환이 중요. but 리스트는 순서가 있기 때문에 제거하는 위치가 정해져 있음 
my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()

print(element) # 1 
print(my_set) # {1, 2, 3, 'b', 'a'}

print('-----')


# s.update(iterable) : 세트에 다른 iterable 요소를 추가
# 리스트의 append랑 extend와 비슷한 친구
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.update([1, 4, 5])
print(my_set) # {'c', 1, 2, 3, 4, 5, 'b', 'a'}

print('-----')


# 세트의 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 5, 3, 9 ,7}

# 차집합
print(set1.difference(set2)) # {0, 2, 4}

# 교집합
print(set1.intersection(set2)) # {1, 3}

# set1 <= set2
print(set1.issubset(set2)) # False

# set1 >= set2
print(set1.issuperset(set2)) # False

# 합집합
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9} -> 정렬도 됨


print('-----')


# 딕셔너리 메서드
'''
- D.clear() : 딕셔너리 D의 모든 키/값 쌍을 제거

- D.get(k) : key k에 연결된 값을 반환(키가 없으면 None을 반환)

- D.get(k, v) : 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환

- D.keys() : 딕셔너리 D의 키를 모은 객체를 반환

- D.values() : 딕셔너리 D의 값을 모은 객체를 반환

- D.items() : 딕셔너리 D의 키/값 쌍을 모은 객체를 반환

- D.pop(k) : 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 
             (없으면 오류)

- D.pop(k, v) : 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 
             (없으면 v를 반환)
- D.setdefault(k) : 딕셔러니 D에서 키 k와 연결된 값을 반환

- D.setdefault(k, v) : 딕셔너리 D에서 키 k와 연결된 값을 반환
                       k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 V를 반환

- D.update(other) : other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을
                    other에 있는 값으로 대체.
                    other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가
'''

# .clear() : 딕셔너리 D의 모든 키/값 쌍을 제거
person = {'name' : 'Alice', 'age' : 25}
person.clear()
print(person) # {}

print('-----')

# .get(key[,default]) : 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
# 중요!!! 
person = {'name' : 'Alice', 'age' : 25}

print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # Unknown

print('-----')

# .items() : 딕셔너리 키/값 쌍을 모은 객체를 반환
person = {'name' : 'Alice', 'age' : 25}

print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])

for k, v in person.items():
    print(k, v)
'''
name Alice
age 25
'''

print('-----')

# .pop(key[,default]) : 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default를 반환)
person = {'name' : 'Alice', 'age' : 25}

print(person.pop('age')) # 25 -> 반환 값을 활용 할 수 있음
print(person) # {'name': 'Alice'}

print(person.pop('country', None)) # None
# print(person.pop('country')) # KeyError

print('-----')


# .setdefault(key[,default]) : 키와 연결된 값을 반환.
#                              키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
person = {'name' : 'Alice', 'age' : 25}

print(person.setdefault('country', 'KOREA')) # KOREA -> 키와 연결된 값을 반환
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

print('-----')


# .update([other]) : other가 제공하는 키/값 쌍으로 딕셔너리를 갱신.
#                    기존 키는 덮어씀. 둘 다 없으면 키/값 쌍으로 추가
person = {'name' : 'Alice', 'age' : 25}
other_person = {'name':'Jane', 'gender':'Female'}

person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=50)
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female'}

person.update(country='KOREA')
print(person)  # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}
# -> 키/값이 존재하지 않아서 딕셔너리에 키/값 쌍으로 추가됨.





