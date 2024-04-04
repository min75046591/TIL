"""
탈주범은 시간당 1의 거리를 움직일 수 있음
중복 가능 -> 지나간 장소 다시 갈 수 있음, 한 자리에 계속 있을 수 있음
-> 지나갈 수 있는 곳은 다 세기
"""
from collections import deque

def catch(i, j, s):
    visited[i][j] = 1    #  방문 표시
    if s == L:           # 시간이 다 됐을 때
        return

    # 1. 상 (1, 2, 4, 7)일 경우에 가능
    if (i-1 >= 0 and (cage[i][j] == 1 or cage[i][j] == 2 or cage[i][j] == 4 or cage[i][j] == 7)
            and visited[i-1][j] == 0
            and (cage[i-1][j] == 1 or cage[i-1][j] == 2 or cage[i-1][j] == 5 or cage[i-1][j] == 6)):
        visited[i-1][j] += 1     # 방문표시
        catch(i-1, j, s+1)           # 이동
        visited[i-1][j] = 0     # 방문 초기화

    # 2. 하 (1, 2, 5, 6)일 경우에 가능
    if (i+1 < N and (cage[i][j] == 1 or cage[i][j] == 2 or cage[i][j] == 5 or cage[i][j] == 6)
            and visited[i+1][j] == 0
            and (cage[i+1][j] == 1 or cage[i+1][j] == 2 or cage[i+1][j] == 4 or cage[i+1][j] == 7)):
        visited[i+1][j] += 1     # 방문표시
        catch(i+1, j, s+1)           # 이동
        visited[i+1][j] = 0     # 방문 초기화

    # 3. 좌 (1, 3, 4, 5)일 경우에 가능
    if (j-1 >= 0 and (cage[i][j] == 1 or cage[i][j] == 3 or cage[i][j] == 4 or cage[i][j] == 5)
            and visited[i][j-1] == 0
            and (cage[i][j-1] == 1 or cage[i][j-1] == 3 or cage[i][j-1] == 6 or cage[i][j-1] == 7)):
        visited[i][j-1] += 1     # 방문표시
        catch(i, j-1, s+1)           # 이동
        visited[i][j-1] = 0     # 방문 초기화

    # 4. 우 (1, 3, 6, 7)일 경우에 가능
    if (j+1 < M and (cage[i][j] == 1 or cage[i][j] == 3 or cage[i][j] == 6 or cage[i][j] == 7)
            and visited[i][j+1] == 0
            and (cage[i][j+1] == 1 or cage[i][j+1] == 3 or cage[i][j+1] == 4 or cage[i][j+1] == 5)):
        visited[i][j+1] += 1     # 방문표시
        catch(i, j+1, s+1)           # 이동
        visited[i][j+1] = 0     # 방문 초기화


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
            if visited[k][l] > 0:
                cnt += 1

    print(f'#{tc} {cnt}')
