'''
최고점과 최저점의 간격을 줄이는 작업
작업 후 최고점과 최저점의 차이를 반환
dump : 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업
가로 = 100
상자 높이 = 1이상 100이하
덤프 횟수 = 1이상 1000이하
'''
T = 10
for tc in range(1, T+1):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump): # 평탄화 작업 반복 수
        max_box = 0
        min_box = 101
        for j in range(100):  # 각 위치의 박스중 최대, 최소 인덱스 확인
            if max_box < arr[j]:
                max_box = arr[j]
                max_index = j  # 가장 높은 박스가 있는 위치
            
            if min_box > arr[j]:
                min_box = arr[j]
                min_index = j   # 가장 낮은 박스가 있는 위치
        
        # 가장 높은 박스중 하나를 낮은 박스 위치로 옮기기 
        arr[max_index] -= 1
        arr[min_index] += 1

    # 평탄화 후 가장 높은 박스와 낮은 박스의 높이 차이
    max_box = 0
    min_box = 101
    for k in range(100):
        if max_box < arr[k]:
            max_box = arr[k]
        if min_box > arr[k]:
            min_box = arr[k]
        result = max_box - min_box
    print(f'#{tc} {result}')