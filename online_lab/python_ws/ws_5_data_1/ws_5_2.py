# 아래 함수를 수정하시오.
def remove_duplicates(og_list):
    new_lst = []
    new_lst.extend(list(set(og_list)))
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)