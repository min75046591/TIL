
# try:
#     num = int(input('숫자입력 :'))
# except ValueError:
#     print('숫자가 아닙니다.') 

try:
    num = int(input('100으로 나눌 값을 입력하시오 :'))
    print(100 / num)

except ValueError:
    print('숫자 입력해라 장난치지말고')

except ZeroDivisionError:
    print('0으로 나누기가 되겠냐?')

except:
    print('알수없는 에러 발생')