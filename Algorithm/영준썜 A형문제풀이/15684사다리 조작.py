def f(N, H):
    for j in range(1, N+1): # 세로선 별로 검토
        v = j
        for i in range(1, H+1): # 가로선 따라 이동
            if hor[i][v]==1: # 오른쪽 이동 가능
                v += 1
            elif hor[i][v-1]==1: # 왼쪽 이동 가능
                v -= 1
        if v!=j: # 다른 세로선으로 나오면 중단
            return 0
    return 1

def f2(N, H):
    goal = [x for x in range(N + 1)]  # 각 세로선에서 출발한 경우 i에서의 위치
    for i in range(1, H + 1):  # 가로선 위치
        for j in range(1, N + 1):  # 출발점 j기준 i에서의 위치
            if hor[i][goal[j]] == 1:  # 오른쪽으로 이동할 가로선이 있으면
                goal[j] += 1  # 오른쪽 세로선으로 이동
            elif hor[i][goal[j] - 1] == 1:  # 왼쪽으로 이동할 가로선이 있으면
                goal[j] -= 1  # 왼쪽 세로선으로 이동
    for i in range(1, N + 1):
        if goal[i] != i:
            return 0
    return 1

def ladder(N, H):
    if f(N, H): # 추가없이 완료
        return 0
    for i in range((N-1)*H): # 가로선 1개 추가
        if hor[i//(N-1)+1][i%(N-1)]==0 and hor[i//(N-1)+1][i%(N-1)+1]==0:
            hor[i//(N-1)+1][i%(N-1)+1]=1 # 가로선 추가
            if f(N, H):
                return 1
            hor[i // (N - 1) + 1][i % (N - 1) + 1] = 0

    for i in range((N-1)*H-1): # 가로선 위치 선택
        if hor[i//(N-1)+1][i%(N-1)]==0 and hor[i//(N-1)+1][i%(N-1)+1]==0:
            hor[i//(N-1)+1][i%(N-1)+1]=1 # 가로선 추가
            for j in range(i+1, (N-1)*H):
                if hor[j//(N-1)+1][j%(N-1)] == 0 and hor[j//(N-1)+1][j%(N-1)+1] == 0:
                    hor[j//(N-1)+1][j%(N-1)+1] = 1  # 가로선 추가
                    if f(N, H):
                        return 2
                    hor[j // (N - 1) + 1][j % (N - 1) + 1] = 0  # 가로선 삭제
            hor[i//(N-1)+1][i%(N-1)+1] = 0  # 가로선 삭제
    for i in range((N-1)*H-2): # 가로선 위치 선택
        if hor[i//(N-1)+1][i%(N-1)]==0 and hor[i//(N-1)+1][i%(N-1)+1]==0:
            hor[i//(N-1)+1][i%(N-1)+1]=1 # 가로선 추가
            for j in range(i+1, (N-1)*H-1):
                if hor[j//(N-1)+1][j%(N-1)] == 0 and hor[j//(N-1)+1][j%(N-1)+1] == 0:
                    hor[j//(N-1)+1][j%(N-1)+1] = 1  # 가로선 추가
                    for k in range(j+1, (N-1)*H):
                        if hor[k // (N - 1) + 1][k % (N - 1)] == 0 and hor[k // (N - 1) + 1][k % (N - 1) + 1] == 0:
                            hor[k // (N - 1) + 1][k % (N - 1) + 1] = 1  # 가로선 추가
                            if f(N, H):
                                return 3
                            hor[k // (N - 1) + 1][k % (N - 1) + 1] = 0
                    hor[j // (N - 1) + 1][j % (N - 1) + 1] = 0
            hor[i // (N - 1) + 1][i % (N - 1) + 1] = 0  # 가로선 삭제
    return -1


# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
N, M, H = map(int, input().split())  # 2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H
hor = [[0]*(N+2) for _ in range(H+1)] # 가장자리 정보 추가

for _ in range(M):
    a, b = map(int, input().split())
    hor[a][b] = 1 # 미리 주어진 가로선
# 0, 1, 2, 3개의 가로선을 각각 추가하고 사다리타기 진행
if M==0:
    print(0)
else:
    ans = ladder(N, H)
    print(ans)