# 완전 검색 그리디
T = int(input())
for tc in range(1, T+1):
    num = list(map(int, list(input())))
    c = [0]*12  # 인덱스 11까지 만들어 마지막 인덱스인 9까지 탐색
    for i in range(6):
        c[num[i] % 10] += 1 # 10으로 나눈 나머지를 인덱스로 사용하여 해당 리스트에 숫자의 개수를 1증가
    # 트리플렛과 런 조사
    i = 0
    tri = runn = 0
    while i < 10:
        if c[i] >= 3: # c[i]에 해당하는 숫자의 개수가 3개 이상일때
            c[i] -= 3  # 숫자의 개수 3 제거
            tri += 1  # 트리플렛 1 추가
            continue # 다시 위로 올라가서 트리플렛 검사

        #런 조사
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            runn += 1
            continue
        i += 1

    if tri + runn == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')