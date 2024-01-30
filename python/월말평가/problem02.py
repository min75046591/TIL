############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len, sum 함수를 사용하지 않습니다.
def average_cost(cost_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    total = 0
    for average in cost_list:
        total += average
    
    # 빈 변수에 cost_list가 들어갈 때마다 +1을 해줘서 길이를 잼
    # -> len_list에 cost_list의 길이값을 할당 
    len_list = 0
    for _ in cost_list:
        len_list += 1
    
    # total의 실수형을 요소의 개수로 나누기
    return float(total)/len_list


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_cost([25, 40, 50, 55]))  # 42.5
print(average_cost([60, 70, 90, 80, 100, 35])) # 72.5
#####################################################
