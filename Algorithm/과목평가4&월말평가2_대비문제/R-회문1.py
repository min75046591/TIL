"""
똑바로 읽든 거꾸로 읽든 똑같은 문장이나 낱말을 회문
회문의 개수를 구해라
8x8 크기
"""
T = 10
for tc in range(1, T+1):
    N = int(input())        # 찾아야 하는 회문의 길이
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    # 가로 확인
    for i in range(8):
        for j in range(8-N+1):
            str_1 = ''
            str_2 = ''
            # 해당하는 범위의 문자 변수에 넣기
            for k in range(N):
                str_1 += arr[i][j+k]
                str_2 += arr[j+k][i]
            # 추출한 문자열이 거꾸로 했을때 같은지
            if str_1 == str_1[::-1]:
                cnt += 1
            if str_2 == str_2[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')
