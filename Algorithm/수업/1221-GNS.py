T = int(input())
for tc in range(1, T+1):
    tn, list_length = input().split()
    list_length = int(list_length) # 정수형으로 형변환
    tmp_num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 문자들 입력 받기
    str_nums = list(input().split())
    # 카운팅 로직 만들기
    # 딕셔너리를 만들어서 로직을 짜기
    # 영어를 키로 개수를 값으로
    # for 문을 돌면서 result에 더해주기
    tmp_dict = {}
    for i in str_nums:
        if i in tmp_dict:
            tmp_dict[i] += 1
        else:
            tmp_dict[i] = 1
    result = ''
    for j in tmp_num_list:
        result += tmp_dict[j] * (j + ' ')  # tmp_dict = j에 해당하는 value
    print(f'#{tc}\n{result}')