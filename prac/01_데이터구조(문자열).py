string1 = 'Hello'
string2 = '12a3'


# isalpha : 문자열이 전부 알파벳인가?
print(string1.isalpha()) # True
print(string2.isalpha()) # False

'''
- s.islower() : 문자열이 전부 소문자인가?
- s.isupper() : 문자열이 전부 대문자인가?
'''
print(string1.isupper()) # False
print(string2.islower()) # True

'''
- s.find(x) : x의 첫 번째 위치를 반환. 없으면 -1 반환
- s.index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생
 -> ValueError: substring not found
'''

print('-----')

# 문자열 조작 메서드 (새 문자열 반환)
'''
- s.replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 return
- s.strip([chars]) : 공백이나 특정 문자를 제거
- s.split(sep='구분자', maxsplit=분할 횟수)
- 'separator'.join([iterable]) : 구분자로 iterable을 합침
- s.capitalize() : 가장 첫 번째 글자를 대문자로 변경
- s.title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로,
              나머지는 소문자로 변환
- s.upper() : 모두 대문자로 변경
- s.lower() : 모두 소문자로 변경
- s.swapcase() : 대<->소문자 서로 변경
'''

# 실행해보기!

# .replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
# -> [,count] 는 세 번째 인자로 선택인자다. 앞에 두개는 필수고 카운트는 선택사항.
text = 'Hello, world'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python

print('-----')

# .strip([chars]) : 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
# -> [chars] 는 선택사항. 안쓰면 공백 제거. 사용하면 지정한 문자를 제거
text = '  Hello, world!     '
new_text = text.strip()
new_text2 = new_text.strip('!') # -> 공백도 같이 제거됨
print(new_text) # Hello, world!
print(new_text2) # Hello, world

print('-----')

# split(sep=None, maxsplit=-1) : 지정한 문자를 구분자로 문자열을 분리하여
#                                문자열의 리스트로 반환
text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', ' world!'] -> 콤마를 기준으로 나눠진 후 리스트에 반환됨.

print('-----')


# 'separator'.join([iterable]) : iterable 요소들을 원래의 문자열을 구분자로 이용하여
#                                하나의 문자열로 연결. split의 반대
words = ['Hello', 'world!']
text = '-'.join(words)
text2 = ', '.join(words)  # -> 띄어쓰기(공백)도 들어감

print(text)  # Hello-world!
print(text2)  # Hello, world! 

print('-----')

# 나머지 .capitalize(), .title(), .upper(), .swapcase()
text = 'heLLo, woRld!'
new_1 = text.capitalize()
new_2 = text.title()
new_3 = text.upper()
new_4 = text.swapcase()

print(new_1) # Hello, world! -> 처음 시작만 대문자
print(new_2) # Hello, World! -> 각 문자열 맨 앞자리들만 대문자
print(new_3) # HELLO, WORLD! -> 싹다 대문자
print(new_4) # HEllO, WOrLD! -> 대<->소문자 변경됨

print('-----')

# 메서드는 이어서 사용 가능. but 앞쪽 메서드가 반환값이 없는 None이면 이어갈 수 없음.
text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text) # HEzzO, WOrLD!