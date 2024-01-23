# my_set = {}  # 빈 딕셔너리
# # 비슷한점 주의!!
# my_set = set()  # 이게 빈 세트

my_set = {'a', 'b', 'c', 1, 2, 3}
# 1. set는 순서가 존재하지 않음
# 2. 어떻게 그 값에 접근할 수 있는지?

my_set.add(4)  # 한번 더 add를 하더라도 중복된 값이 들어가진 않음
print(my_set)

my_set.add(4)
print(my_set)

my_set.remove('a')  # 존재하지 않는 요소를 지우려하면 KeyError 뜸
print(my_set)

element = my_set.pop()  # 세트에서 임의의 요소를 제거하고 반환
print(element)

my_set.update([1, 4, 5])
print(my_set)

my_set.discard(1)
print(my_set)

my_set.discard('z')  # 요소에 없더라도 아무런 반응이 없음. remove와 달리 에러 없음
print(my_set)

# my_set.clear()
# print(my_set)

set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}  
set3 = {0, 1}  

print(set1.difference(set2))   # 차집합 set1 - set2
print(set1.intersection(set2)) # 교집합 set1 & set2
print(set1.issubset(set2))   # set2 가 set1을 포함하는지
print(set1.issuperset(set2))  # set1 이 set2를 포함하는지
print(set1.issuperset(set3))
print(set1.union(set2))     # 합집합