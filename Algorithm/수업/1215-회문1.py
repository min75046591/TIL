T = int(input())
for tc in range(1, T+1):
    M = int(input())  # 찾아야 하는 회문의 길이
    N = 8             # N*N 맵 / 문장의 길이 / 행 또는 열의 길이
    txt = [input().split() for _ in range(N)]
    cnt = 0
    # 가로 검사
    for i in range(N):      # 가로축으로 한줄씩 i에 담음
        for j in range(N-M+1):    # 부분 문자열을 추출할 수 있는 시작 위치의 범위
            if txt[i][j:j+M] == txt[i][j:j+M][::-1]:
                cnt += 1
            break

    # 세로 검사
    for j in range(N-M+1):
        for i in range(N):
            vertical = ''
            for x in range(i, i+M):
                vertical += txt[x][j]
            if vertical == vertical[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')