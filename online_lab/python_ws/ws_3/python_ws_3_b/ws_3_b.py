# global의 pro_num 변수에 담긴 값이 1 증가하여야 한다.
pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}


# create_data 함수를 정의
def create_data(subject, day, title=None):
    global pro_num
    data = {'과목':subject,'일차':day,'제목':title,'문제 번호':pro_num+1}
    pro_num += 1
    return data


result_1 = create_data('python', 3)
result_2 = create_data('문자열 web', 1, 'web 연습하기')
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)