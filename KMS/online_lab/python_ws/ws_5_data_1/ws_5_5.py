# 아래 함수를 수정하시오.
def even_elements(num_list):
    result_list = []
    while num_list:
        r = num_list.pop(0)
        if r % 2 == 0:
            result_list.extend([r])
    return result_list    


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
