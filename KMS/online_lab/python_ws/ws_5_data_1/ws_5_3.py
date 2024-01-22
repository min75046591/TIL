# 아래 함수를 수정하시오.
def sort_tuple(tuple_list):
    new_tuple = tuple(sorted(tuple_list))         # list 외엔 sorted
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
