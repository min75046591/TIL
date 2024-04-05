from collections import deque

def catch(i, j, s):
    d = deque([(i, j)])    # 시작 위치 인큐
    visited[i][j] = 1    #  방문 표시

    if s == L:           # 시간이 다 됐거나 더 이상 갈 곳이 없을 때
        return

    # 상(1,2,5,6) 하(1,2,4,7) 좌(1,3,4,5) 우(1,3,6,7) 로만 갈 수 있음
    # 1. 상 (1, 2, 4, 7)일 경우에 가능
    if (i-1 >= 0 and (cage[i][j] == 1 or cage[i][j] == 2 or cage[i][j] == 4 or cage[i][j] == 7)
            and visited[i-1][j] == 0
            and (cage[i-1][j] == 1 or cage[i-1][j] == 2 or cage[i-1][j] == 5 or cage[i-1][j] == 6)):
        d.append((i-1, j))      # 이동 시
        visited[i-1][j] = 1     # 방문표시
        catch(i-1, j, s+1)           # 이동
    else:
        return

    # 2. 하 (1, 2, 5, 6)일 경우에 가능
    if (i+1 < N and (cage[i][j] == 1 or cage[i][j] == 2 or cage[i][j] == 5 or cage[i][j] == 6)
            and visited[i+1][j] == 0
            and (cage[i+1][j] == 1 or cage[i+1][j] == 2 or cage[i+1][j] == 4 or cage[i+1][j] == 7)):
        d.append((i+1, j))      # 이동 시
        visited[i+1][j] = 1     # 방문표시
        catch(i+1, j, s+1)           # 이동
    else:
        return

    # 3. 좌 (1, 3, 6, 7)일 경우에 가능
    if (j-1 >= 0 and (cage[i][j] == 1 or cage[i][j] == 3 or cage[i][j] == 6 or cage[i][j] == 7)
            and visited[i][j-1] == 0
            and (cage[i][j-1] == 1 or cage[i][j-1] == 3 or cage[i][j-1] == 4 or cage[i][j-1] == 5)):
        d.append((i, j-1))      # 이동 시
        visited[i][j-1] = 1     # 방문표시
        catch(i, j-1, s+1)           # 이동
    else:
        return

    # 4. 우 (1, 3, 4, 5)일 경우에 가능
    if (j+1 < M and (cage[i][j] == 1 or cage[i][j] == 3 or cage[i][j] == 4 or cage[i][j] == 5)
            and visited[i][j+1] == 0
            and (cage[i][j+1] == 1 or cage[i][j+1] == 3 or cage[i][j+1] == 6 or cage[i][j+1] == 7)):
        d.append((i, j+1))      # 이동 시
        visited[i][j+1] = 1     # 방문표시
        catch(i, j+1, s+1)           # 이동
    else:
        return


T = int(input())
for tc in range(1, T+1):
    # 터널 지도의 세로 N, 가로 M, 맨홀 뚜껑이 위치한 장소의 세로 R, 가로 C, 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    cage = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0      # 탈주범이 위치 할 수 있는 장소의 개수
    catch(R, C, 0)  # 시작 위치

    # 방문 위치 찾기
    for k in range(N):
        for l in range(M):
            if visited[k][l] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')
