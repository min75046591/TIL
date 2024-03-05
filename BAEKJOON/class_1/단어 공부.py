"""
알파벳 대소문자로 된 단어
가장 많이 사용된 알파벳이 무엇인지
대문자와 소문자를 구분하지 않는다.

가장 많이 사용된 알파벳을 대문자로 출력

대문자를 소문자로 바꿔서 카운트
"""
s = input().lower() # 소문자로 뽑기
s_set = list(set(s))    # 집합화해서 중복제거
cnt = []
for i in s_set:     # m, i ,s ,p 하나씩 cnt 리스트에 추가
    cnt.append(s.count(i))  # [1, 4, 4, 1]

max_v = max(cnt)
if cnt.count(max_v) >= 2:
    print('?')
else:
    print(s_set[cnt.index(max_v)].upper())


"""
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])
"""