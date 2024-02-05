T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_map = [list(map(int, input().split()) for _ in range(N))]
    di = [0, -1, 0, 1]  # 상 하
    dj = [-1, 0, 1, 0]  # 좌 우
    sum_list = []  # 보너스 점수를 모아놓을 공간

    for i in range(1, N-1):
        for j in range(1, N-1):
            tmp = []  # 상하좌우의 값을 넣을 공간
            didj_sum = 0 # 상하좌우의 값
            for k in range(4):
                for l in range(4):
                    ni = i + di[k] # 다음으로 이동할 행
                    nj = j + dj[k] # 다음으로 이동할 열
                    if 0 < ni < N and 0 < nj < N: # 만약 다음으로 이동한 위치가 0보다 크고 N 미만이면 이동.
                        didj_sum = di + dj
                        tmp.append(didj_sum)  # 상하좌우 위치에 해당하는 값을 tmp에 넣는다

                for num in tmp: # tmp 에 담긴 숫자들을 보너스 점수에 다 더한다.
                    bonusnum = 0  # 보너스 점수 초기화
                    if bonusnum > 0:  # 보너스 점수가 양수일때
                        bonusnum += num
                        if bonusnum % 2 == 0:  # 보너스 점수가 짝수라면 점수에 2를 곱한다.
                            bonusnum *= 2
                            sum_list.append(bonusnum) # 점수를 더한값을 모으는 리스트에 넣기
                        else: # 홀수일땐 그냥 sum_list에 넣기
                            bonusnum += num
                            sum_list.append(bonusnum)
                    else:  # 0이거나 음수일 때
                        bonusnum = 0
# sum_list에 담겨있는 보너스 점수들중 가장 큰 값 구하기
    max_score = 0
    for max_v in sum_list:
        if max_score < max_v:
            max_score = max_v
    print(f'#{tc} {max_score}')




