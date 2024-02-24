"""
어떤 구역에 이웃한 오른쪽의 고구마 개수가 더 많으면, 두 구역의 모든 고구마가 하나의 줄기에 매달려 있음
두개 이상의 구역에 걸쳐 있는 줄기를 '긴 줄기'라 이름을 붙임

고구마밭에 총 몇개의 '긴 줄기'가 있는가. 그리고 가장 긴 줄기에 달린 고구마의 개수

가장 긴 줄기기 여럿일 땐 고구마의 개수가 많은 쪽을 긴 줄기로 선택
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    box = []
    result = []
    long_stem = 0

    for i in range(N-1):
        # 내 오른쪽 영역의 고구마가 더 많다면
        if arr[i] < arr[i+1]:
            long_stem += arr[i] + arr[i+1]
            box.append(long_stem)

        if arr[i] > arr[i+1]:
            result.append(box)
            long_stem = 0

    print(result)

    output_1 = len(result)
    output_2 = 0
    for k in result:
        if output_2 < k:
            output_2 = k
    #print(f'#{tc} {output_1} {output_2}')

