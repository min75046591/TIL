"""
보너스 단계에 도달, 한발의 총알 사용 가능
어떤 칸을 맞추면 상화좌우 각 방향으로 두칸 씩 점수. 자기 자리도 포함
상하좌우 중 일부 칸이 없는 경우, 존재하는 칸의 점수만 비교
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    score = 0
    for i in range(N):              # arr 범위 탐색
        for j in range(N):
            score = 0               # 움직일때마다 저장할 점수 변수 초기화
            score += arr[i][j]      # 자기 위치 점수 넣기
            for p in range(1, 3):   # i j 위치에서 상하좌우 두 칸씩 넣어야 하기 때문에
                # 상 하 좌 우
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i+di*p, j+dj*p         # 상하좌우 두칸 범위 안 탐색
                    if 0 <= ni < N and 0 <= nj < N:     # 탐색 위치 제한 설정
                        score += arr[ni][nj]            # 점수 변수에 상하좌우 범위 값 더하기
            if max_v < score:   # 점수가 최대값 보다 크면 max_v에 점수 저장
                max_v = score


    print(f'#{tc} {max_v}')


