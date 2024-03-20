"""
우승하면 보너스 상금

우승자는 주어진 숫자판들 중에 두 개를 선택해서 정해진 횟수만큼 서로의 자리를 위치를? 교환할 수 있다.

정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산
오른쪽 끝부터 1원. 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커짐
-> 가장 왼쪽부터 큰 숫들로 정렬

반드시 교환 횟수만큼 교환해야함

교환했을 때 가장 큰 금액

"""

# 순열 확인 (자리 바꾸기)
def dfs(x):
    global max_cost
    if x == c:  # c번 교환
        max_cost = max(max_cost, int("".join(map(str, nums))))  # 최댓값 비교
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            nums[i], nums[j] = nums[j], nums[i]  # 자리 바꾸기

            chk = int("".join(map(str, nums)))
            if (x, chk) not in path:  # 가지치기 (지나간 자리가 아니면)
                dfs(x + 1)  # x+=1
                path.append((x, chk))  # 흔적 남기기

            nums[i], nums[j] = nums[j], nums[i]  # 초기화


T = int(input())
for tc in range(1, T + 1):
    tmp, c = input().split()
    c = int(c)
    N = len(tmp)
    nums = []  # 순열 리스트 초기화
    path = []  # 흔적 리스트 초기화
    max_cost = 0  # 최댓값 초기화
    for i in tmp:
        nums.append(i)
    dfs(0)
    print(f'#{tc} {max_cost}')
