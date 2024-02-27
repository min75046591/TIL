def perm(i, k, M):  # p[i]를 채워서 k개의 숫자로 만드는 순열, 인덱스가 사전순으로 생성
    if i == k:
        print(p)
    else:
        for j in range(M):  # 모든 원소에 대해 주어진 원소가 M개 (k<=M)
            if used[j] == 0:  # 사용된 적이 없으면
                p[i] = arr[j]  # 순열에 사용
                used[j] = 1  # 사용됨으로 표시
                perm(i + 1, k, M)
                used[j] = 0  # 다른 자리에서 사용가능


M = 5  # 주어진 숫자 개수
arr = [1, 2, 3, 4, 5]
N = 3  # 만들 순열의 길이
p = [0] * N
used = [0] * M
perm(0, N, M)