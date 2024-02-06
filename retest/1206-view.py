for test_case in range(1, 10 + 1):
    n = int(input())
    building_li = list(map(int, input().split()))
    result = 0
    # 4개의 건물 중 가장 높은 건물을 찾아서, 가운데 빌딩(i)와 비교한다.
    for i in range(2, len(building_li) - 2):  # 앞에 두칸과 뒤에 두칸 빈공간 반영
        max_v = 0
        for j in range(i - 2, i + 2 + 1):
            if not i == j:
                if max_v < building_li[j]:
                    max_v = building_li[j]
        if max_v < building_li[i]:
            result += (building_li[i] - max_v)

    print(f'#{test_case} {result}')
