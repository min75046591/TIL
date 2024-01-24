# 계산기 함수 만들기
# 결과값
# print(add_cal(3))
# print(add_cal(4))

result = 0

def add_cal(num):
    global result
    result = result + num
    return result

result = add_cal(3)
print(result)

print(add_cal(4))

# 이러한 함수를 각각 다른 반에게 적용하기 위해 계속 만들면 코드의
# 비효율성이 생김. 따라서 클래스를 선언해서 하는게 더 효율적이라
# 클래스를 선언하는거임.