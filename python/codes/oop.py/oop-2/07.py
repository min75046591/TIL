# 딕셔너리에서 키를 조회할 때
# 키가 없다는 상황
my_dict = {}


# try-except
try:
    result = my_dict['a']
    print(result)
except KeyError:
    print('key가 존재하지 않습니다.')


# if-else
if 'a' in my_dict:
    result = my_dict['a']
    print(result)
else:
    print('key가 존재하지 않습니다.')