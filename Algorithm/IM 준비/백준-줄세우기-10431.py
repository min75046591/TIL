"""
키 순서대로 번호
반 아이들은 항상 20명
같은 키를 가신 학생은 없다

우선 아무나 한 명을 뽑아 줄의 맨 앞에 세운다
1. 자기 앞에 자기보다 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다
2. 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
이때, A부터 그 뒤의 모든 학생들은 한 칸씩 뒤로 감

마지막 학생까지 시행하여 줄서기가 끝났을 때 학생들이 총 몇번 뒤로 물러서게 되는가!
나보다 키 큰 학생이 앞에 한 명 이상 있으면
내가 맨 앞으로 갔을 때 지금까지 서있던 학생들의 수를 cnt에 더해준다
"""
T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 20):
        for j in range(i):
            if arr[i] < arr[j]:
                cnt += 1
    print(f'{arr[0]} {cnt}')



T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    cnt = 0     # 뒤로 물러난 횟수
    for i in range(1, 20):    # 1번 ~ 19번
        for j in range(i+1, 20+1):  # i+1 ~ 20번
            if arr[i] > arr[j]: # 자신보다 큰 학생이 앞에 을 때
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1

    print(f'{arr[0]} {cnt}')
