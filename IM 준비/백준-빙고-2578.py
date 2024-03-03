"""
철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때
사회자가 몇 번째 수를 부른 후 철수가 '빙고'를 외치게 되는지 출력하라

F A I L
실패!!!!!!!!!!!

"""
arr = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자 : list (1차원으로 생성 / 저장)
man_list = []
for _ in range(5):
    man_list += list(map(int, input().split()))

result = 0
# 사회자가 부르는 숫자 0으로 바꾸기
for n in range(len(man_list)):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == man_list[n]:
                arr[i][j] = 0       # 사회자가 부른 숫자가 있으면 0으로 지우기

                # for k in range(5):
                #     for l in range(5):
                #         if arr[k][l] == 0:
                #
                for di, dj in [[-1, 1], [0, 1], [1, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [1, -1]]:
                    cnt = 1
                    ni, nj = i+di, j+dj
                    while 0<=ni<5 and 0<=nj<5 and arr[ni][nj] == 0:
                        cnt += 1
                        if cnt == 5:
                            result = n
                            break
                        ni, nj = ni+di, nj+dj

print(result)