T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    cnt = 0
    i = 0   # A에서 비교 시작 위치
    j = 0   # B에서의 비교 위치
    while i <= N - M:   # B의 길이만큼인 마지막 구간의 시작 위치
        if A[i+j] == B[j]:  # 같은 글자면
            j += 1
            if j == M:  # B의 마지막 글자인 경우
                cnt += 1    # 단축키 횟수
                j = 0   # 패턴을 찾은 경우
                i += M
        else:
            j = 0
            i += 1
    print(f'#{tc} {N - M * cnt + cnt}')







'''
두번째 case

t = int(input())

for test_case in range(1, t + 1):
    word, short_word = map(str, input().split())
    length_word = len(word)
    length_short_word = len(short_word)
    short_word_count = 0
    word_index = 0

    while word_index < length_word:
        if word[word_index:word_index + length_short_word] == short_word:
            short_word_count += 1
            word_index += length_short_word
        else:
            word_index += 1

    result = length_word - (length_short_word - 1) * short_word_count

    print(f'#{test_case} {result}')
'''







'''
세번째 case

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()

    count = 0
    while B in A:  # B가 A 안에 있을 때,
        A = A.replace(B, '', 1)  # B의 문자를 1번만 없애고,
        """
        이때, A로 할당을 해주지 않으면, replace() 가 반영 x
        """
        count += 1  # 이때, count +1을 해준다.

    result = len(A) + count
    print(f'#{tc} {result}')
'''