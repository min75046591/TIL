T = int(input())
for tc in range(1, T + 1):
    word = input()
    N = len(word)
    ans = 0
    for i in range(N//2):
        if word[i] == word[N-1-i]:  # 0과 4/ 1과 3 ...
            ans = 1
            break
    print(f'#{tc} {ans}')

def palindrome(word):
    for i in range(N//2):
        if word[i] != word[N-1-i]:
            return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    words = input()
    N = len(words)
    result = palindrome(words)
    print(f'#{tc} {result}')