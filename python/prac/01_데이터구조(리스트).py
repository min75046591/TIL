# 리스트 값 추가 및 삭제 메서드
'''
- L.append(x) : 리스트 마지막에 항목 x를 추가
- L.extend(m) : iterable m의 모든 항목들을 리스트 끝에 추가 
                (+= 과 같은 기능)
- L.insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입
- L.remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거
                항목이 존재하지 않을 경우, ValueError
- L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
- L.pop(i) : 리스트 인덱스 i에 있는 항목을 반환 후 제거
- L.clear() : 리스트의 모든 항목 삭제
'''

# L.append(x) : 리스트 마지막에 항목 x를 추가
my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.append([9, 8, 0, 2])
print(my_list) # [1, 2, 3, 4, 5, [9, 8, 0, 2]] -> 1. 리스트 마지막에 5추가 / 2. 추가된 5 뒤에 리스트 추가
print(my_list.append([1, 2])) # None

print('-----')

# L.extend(iterable) : 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
#                      반복 가능한 객체 : list, str, tuple, dict, set, range등
my_list = [1, 2, 3]
my_list.extend([3, 4, 5, 6])
print(my_list) # [1, 2, 3, 3, 4, 5, 6]
my_list.extend(range(2))
print(my_list) # [1, 2, 3, 3, 4, 5, 6, 0, 1]

print('-----')

# L.insert(i, x) : 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
my_list = [1, 2, 3]
my_list.insert(2, 9)
print(my_list) # [1, 2, 9, 3] -> 위치의 값을 변환하는게 아닌 위치에 값을 추가

print('-----')

# L.remove(x) : 리스트에서 첫 번째로 일치하는 항목을 제거
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list) # [1, 3]

print('-----')

# L.pop(i) : 리스트에서 지정한 인덱스의 항목을 제거하고 반환.
#            작성하지 않을 경우 마지막 항목을 제거
my_list = [1, 2, 3, 4, 5]

item1 = my_list.pop()
item2 = my_list.pop(0) # 0번째 인덱스의 항목을 제거하고 반환

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]

print('-----')

# L.clear() : 리스트의 모든 항목을 삭제
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []

print('-----')



# 리스트 탐색 및 정렬 메서드
'''
- L.index(x, start, end) : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
- L.reverse() : 리스트의 순서를 역순으로 변경 (정렬 x)
- L.sort() : 리스트를 정렬 (매개변수 이용 가능)
- L.count(x) : 리스트에서 항목 x의 개수를 반환
'''


# L.index(x) : 리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

print('-----')

# L.count(x) : 리스트에서 항목 x가 등장하는 횟수를 반환
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 3

print('-----')

# L.sort() : 원본 리스트를 오름차순으로 정렬
# sorted() : 리스트를 복제 후 오름차순으로 정렬
my_list = [3, 1, 2]
my_list.sort()
print(my_list) # [1, 2, 3]

# 내림차순
my_list.sort(reverse=True)
print(my_list) # [3, 2, 1]

print('-----')

# L,reverse() : 리스트의 순서를 역순으로 변경 (정렬 x)
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list) # [9, 1, 8, 2, 3, 1]

print('-----')



# 할당 (Assignment)
original_list = [1, 2, 3]
copy_list = original_list

copy_list[0] = 'hello'
print(original_list) # ['hello', 2, 3]


# 얕은 복사
# - 리스트 얕은 복사 예시
a = [1, 2, 3]
b = a[:]
print(a, b) # [1, 2, 3] [1, 2, 3]

b[0] = 100
print(a, b) # [1, 2, 3] [100, 2, 3]

print('-----')

# 얕은 복사의 한계
# -> 2중일때는 얕은 복사 불가능. a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨

a = [1, 2, [100, 200]]
b = a[:]

b[2][0] = 999
print(a) # [1, 2, [999, 200]]
print(b) # [1, 2, [999, 200]]

print('-----')


# 깊은 복사
# -> 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함

import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list)  # [1, 2, [1, 2]]
print(deep_copied_list) # [1, 2, [100, 2]]