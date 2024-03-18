# 선생님 강의

# 분할하는 함수
def msort(m):
    if len(m) == 1: # 원소가 하나만 남은 경우
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = msort(left)      # 왼쪽 절반 분할
    right = msort(right)    # 오른쪽 절반 분할

    return merge(left, right)   # 다시 합친 결과

# 병합하는 함수
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = [0] * (len(left) + len(right))
    i = j = 0       # i : 왼쪽 배열에서 비교할 위치, j: 오른쪽 배열에서 비교할 위치

    while i < len(left) and j < len(right):  # 양쪽에 비교할 원소가 있는 경우
        if left[i] < right[j]:
            result[i+j] = left[i]
            i += 1
        else:       # right[j] < left[i]
            result[i+j] = right[j]
            j += 1

    while i < len(left):        # left의 원소만 남은 경우
        result[i+j] = left[i]
        i += 1

    while j < len(right):       # right의 원소만 남은 경우
        result[i+j] = right[j]
        j += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = msort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')

