T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_v = 0   # 최대값 
    for i in str1:
        cnt = 0  # str1의 문자열 하나마다 카운트를 세기
        for j in str2:
            if i == j:
                cnt += 1
        
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')