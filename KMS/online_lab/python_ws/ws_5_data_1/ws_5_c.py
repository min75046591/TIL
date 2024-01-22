def restructure_word(word, arr):
    for i in word:
        if i.isdecimal():
            for num in range(int(i)):
                arr.pop()
        else:
            arr.remove(i)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'  # 잘못된 문장
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'   # 제거 할 대상
arr = []

list(original_word)
arr.extend(list(original_word))
print(arr)

result = restructure_word(word, arr)
print(result)

result = ''.join(arr)
print(result)