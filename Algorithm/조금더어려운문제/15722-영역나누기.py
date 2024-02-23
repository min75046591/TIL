"""
NxN 에 1이상 100이하 자연수
행과 행, 열과 열 사이에 직선을 하나씩 그어 4개의 영역으로 나눴을 때,
각 영역 합의 최대값과 최소값의 차이중 최소값을 구하라!!
각 영역은 반드시 한 개 이상의 원소를 갖는다

힌트1 : A영역의 오른쪽 아래 원소의 인덱스를 정하면 4영역을 나눌 수 있다
힌트2 : DP를 응용할 수 있다
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # A영역 오른쪽 아래 원소의 인덱스 정하기
    min_diff = 40001
    for i in range(N-1):
        for j in range(N-1):
            num_list = []
            A = B = C = D = 0
            # A 영역의 합
            for k in range(i+1):
                for l in range(j+1):
                    A += arr[k][l]
            num_list.append(A)
            # B 영역의 합
            for k in range(i+1):
                for l in range(j+1, N):
                    B += arr[k][l]
            num_list.append(B)
            # C 영역의 합
            for k in range(i+1, N):
                for l in range(j+1):
                    C += arr[k][l]
            num_list.append(C)
            # D 영역의 합
            for k in range(i+1, N):
                for l in range(j+1, N):
                    D += arr[k][l]
            num_list.append(D)
            # 각 영역들의 합을 모은 리스트에서 가장 큰 값과 작은값의 차를 구함
            dif = max(num_list) - min(num_list)

            if min_diff > dif:
                min_diff = dif

    print(f'#{tc} {min_diff}')