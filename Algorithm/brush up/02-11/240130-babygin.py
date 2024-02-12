'''
1부터 9로 구성된 6개의 숫자를 읽어 베이비진을 판단
'''
T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input()))
    c = [0] * 12  # 인덱스 11까지 만들어 마지막 인덱스인 9까지 탐색
    for i in range(6):
        # 10으로 나눈 나머지. 즉 각 숫자의 개수를 파악
        c[num[i] % 10] += 1

    # triplet & runn 초기화
    i = 0
    triplet = runn = 0
    
    while i < 10:
        # triplet
        if c[i] >= 3: # 개수가 3개 이상 = triplet
            c[i] -= 3 # 트리플렛에 추가하고 숫자 개수 차감
            triplet += 1 # 트리플렛 개수 추가
            continue # 또 트리플렛이 있나 위로 올라가 다시 확인

        # runn
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] = -1  # 연속된 수의 개수 1씩 차감
            c[i+1] = -1
            c[i+2] = -1
            runn += 1
            continue
        
        i += 1 # 0~9 까지 탐색

    if triplet + runn == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
