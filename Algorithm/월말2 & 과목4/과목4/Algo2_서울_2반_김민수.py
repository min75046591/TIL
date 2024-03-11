"""
규칙에 맞게 움직일 때 최대값의 합을 구하는 놀이

N*N 크기의 행렬 A에서 M*M 크기의 행렬을 탐색
M*M 행렬에서 최댓값을 찾고 그 최대값의 위치를 시작점으로 설정(시작점은 행렬의 좌측 상단)

만약 시작점이 탐색하는 행렬내에서 최댓값을 가진다면, 행렬 탐색을 종료

최초의 시작점은 (0,0)

범위를 벗어나면 A 범위 내에서만 탐색을 수행

행렬 내 같은 숫자는 없음

파리퇴치 생각하기
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    i = j = 0
    start = arr[i][j]
    sum_num = 0             # 누적합 저장
    max_v = 0               # M 범위 내의 최대값 저장
    for i in range(N):
        for j in range(N):
            max_num = 0     # M*M 을 순회하며 최대값 갱신
            for k in range(M):
                for l in range(M):
                    if max_num < arr[k][l]:     # M*M 을 순회하며 그 값이 최대값인지 비교하며 갱신
                        max_num = arr[k][l]

            if max_v < max_num:     # 범위 내의 최대값을 max_v에 저장
                max_v = max_num
                if max_v == max_num:    # 순회가 완료된 max_num과 현재 max_v가 같을 때
                    break
                else:
                    sum_num += max_v    # 아니라면 누적합에 더하기

    print(f'#{tc} {sum_num}')