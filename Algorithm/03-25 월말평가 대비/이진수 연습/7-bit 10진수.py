import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    N = len(arr)

    print(f'#{tc}', end=' ')
    for i in range(0, N, 7):
        tmp = []
        for j in range(7):
            idx = i+j
            tmp.append(arr[idx])

        # 10진수로 변환
        result = 0
        for k in range(7):
            result += (2**(6-k) * tmp[k])
        print(result, end=' ')
    print() # 각 테케 마다 줄바꿈을 추가하여 다음 테스트 케이스와 구분