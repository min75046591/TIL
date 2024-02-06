# 아래 함수를 수정하시오.
def count_character(text, char_to_count): # 두개의 매개변수
    # text : 문자를 세고자 하는 대상이 되는 텍스트 ('Hello, World')
    # char_to_count : 세고자 하는 특정 문자 ('o')
    result = text.count(char_to_count)
    return result

# 사용 예시:
result = count_character("Hello, World!", "o")
print(result)  # 출력: 2


# def count_character(char_to_count):
#     result.count(char_to_count)
#     return result

# result = count_character("Hello, World!", "o")

# print(result)