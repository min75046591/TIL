"""
문장에서 단어의 개수를 세어라
대문자만 세어보자
"""
arr = input().split()
cnt = 0     # 단어 개수

for i in arr:
    cnt += 1
print(cnt)