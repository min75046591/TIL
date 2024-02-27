"""
어떤 구역에 이웃한 오른쪽의 고구마 개수가 더 많으면, 두 구역의 모든 고구마가 하나의 줄기에 매달려 있음
두개 이상의 구역에 걸쳐 있는 줄기를 '긴 줄기'라 이름을 붙임

고구마밭에 총 몇개의 '긴 줄기'가 있는가. 그리고 가장 긴 줄기에 달린 고구마의 개수

가장 긴 줄기기 여럿일 땐 고구마의 개수가 많은 쪽을 긴 줄기로 선택
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]
    # 긴 줄기
    cnt = 1     # 줄기 길이
    s = 0  # 긴 줄기의 고구마 개수
    l_root = 0  # 긴 줄기 개수
    # 가장 긴 줄기들
    max_cnt = 1     # 가장 긴 줄기
    max_sp = []  # 가장 긴 줄기의 고구마 개수와 길이
    max_sweet = 0   # 가장 긴 줄기들중 가장 많은 고구마 개수


    for i in range(0, N):
        if arr[i] < arr[i+1]:   # 내 위치와 다음 위치 비교
            cnt += 1            # 줄기 길이
            s += arr[i]         # 줄기의 고구마개수 합 구하기

        elif arr[i] > arr[i+1] and cnt > 1:   # 줄기가 끊기고 긴줄기 일때
            s += arr[i] # 끊겼을때의 arr[i]값 넣어주기
            l_root += 1  # 긴줄기에 +1
            if max_cnt <= cnt:  # 가장 긴 줄기
                max_cnt = cnt
                max_sp.append((cnt, s)) # 긴줄기의 길이와 고구마 개수 넣기
                cnt = 1     # 줄기 길이 초기화
                s = 0       # 고구가 개수 초기화

    for k in range(len(max_sp)):
        if max_sp[k][0] == max_cnt:     # 가장 긴 줄기와 max_sp에 담겨있는 줄기의 길이가 같으면
            if max_sweet < max_sp[k][1]:    # 가장 긴 줄기들의 고구마 개수 비교
                max_sweet = max_sp[k][1]

    print(f'#{tc} {l_root} {max_sweet}')
