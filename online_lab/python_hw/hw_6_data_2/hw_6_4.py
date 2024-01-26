# 아래 함수를 수정하시오.
def add_item_to_dict(my_dict):
    new_dict = my_dict.copy()
    new_dict.setdefault('country', 'USA')
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict)
print(result)



# # 아래 함수를 수정하시오.
# def add_item_to_dict():
#     new_dict = dictionary.copy()
#     pass

#     return new_dict


# my_dict = {'name': 'Alice', 'age': 25}
# result = add_item_to_dict(my_dict, 'country', 'USA')
# print(result)
