# 아래 함수를 수정하시오.
# def find_min_max(num_list):
#     min_val = min(num_list)
#     max_val = max(num_list)
#     result = (min_val, max_val)
#     return result


num_list = [3, 1, 7, 2, 5]
# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)


max_val = num_list[0]
min_val = num_list[0]

for num in num_list:
    if num > max_val:
        max_val = num
    elif num < min_val:
        min_val = num

print(min_val, max_val)
