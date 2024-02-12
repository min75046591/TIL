T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    def selection_sort(a, N):
        for i in range(N-1):   # 왜 N-1을 하는거지? -> 비교하고 위치를 바꿔야하기 때문에 끝에 하나를 남겨놓음
            min_idx = i   # 작은 숫자를 가진 인덱스를 첫 번째 인덱스인 i로 가정
            for j in range(i+1, N):
                if a[min_idx] > a[j]:  # 첫 번째 위치의 숫자가 그 이후의 위치의 숫자보다 크면
                    min_idx = j   # 위치 값을 더 작은 숫자의 위치를 가진 j로 바꾸기
                elif a[min_idx] == a[j]:  # 위에서 이하가 아닌 미만으로 범위를 설정했기 때문에
                    continue              # 굳이 elif로 같을 경우를 넣을 필요가 없음
            a[min_idx], a[i] = a[i], a[min_idx]    # 원래 min_idx와 바뀐 min_idx 위치 바꾸기
        return

    selection_sort(arr, N)
    print(f'#{tc}', *arr)