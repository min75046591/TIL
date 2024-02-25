"""
1은 스위치 켜짐
0은 스위치 꺼짐

학생들에게 1이상이고 스위치 개수 이하인 자연수를 하나씩 나눠줌
자신의 성별과 받은 수에 따라 스위치를 조작

남학생 : 스위치 번호가 자기가 받은 수의 배수면 해당하는 번호의 배수 위치의 스위치 상태 바꿈

여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은
스위치를 포함하는 구간을 찾아 그 구간에 속한 스위치의 상태를 모두 바꿈 -> 이때 스위치 개수는
항상 홀수

스위치들의 마지막 상태를 출력

1번부터 20번까지 출력.
21번은 다음 줄 맨 앞에 출력
스위치 상태 사이에 빈칸을 하나씩 둔다.
"""
N = int(input())        # 스위치 개수
arr = list(map(int, input().split()))    # 스위치 배열 상태
stu_nums = int(input())             # 학생 수
stu_info = [list(map(int, input().split())) for _ in range(stu_nums)]    # 학생 성별, 받은 숫자

for i in range(stu_nums):   # 학생 수
    if stu_info[i][0] == 1:      # 남자
        male_num = stu_info[i][1]
        # 스위치 숫자가 뽑은 숫자의 배수면 바꾸기
        for k in range(1, N+1):
            if k % male_num == 0:
                if arr[k-1] == 0:
                    arr[k-1] = 1
                else:
                    arr[k-1] = 0

    elif stu_info[i][0] == 2:     # 여자
        # 뽑은 숫자 저장
        f_num = stu_info[i][1] - 1
        if arr[f_num] == 0:
            arr[f_num] = 1
        else:
            arr[f_num] = 0

        # 좌우 대칭 확인
        left = f_num - 1
        right = f_num + 1
        while 0 <= left and right < N and arr[left] == arr[right]:
            if arr[left] == 0:
                arr[left] = arr[right] = 1
            else:
                arr[left] = arr[right] = 0
            left -= 1
            right += 1

# 출력은 20번까지. 21번부터는 다음 리스트
for i in range(N):
    print(arr[i], end=" ")
    if (i + 1) % 20 == 0:   # 한 줄에 20개씩 출력. 첫 줄은 0~19
        print()