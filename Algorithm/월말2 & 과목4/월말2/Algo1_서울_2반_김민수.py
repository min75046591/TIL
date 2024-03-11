"""
돌 뒤집기
돌의 양면은 각각 흰색과 검은색

N개의 칸에 돌이 한 개씩 들어있음
총 M번 뒤집음. 뒤집기엔 3가지 방식
1. i번째부터 j개의 돌을 뒤집기
2. i번째부터 j개의 돌을 i번째 색으로 바꾸기
3. i번째 돌을 사이에(i돌의 좌 우)두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 두기

뒤집기는 가능한 돌에 대해서만 진행

흰색 0 , 검은색 1

"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 첫 줄의 돌의 개수,  M 뒤집기 작업의 총 횟수
    arr = [-1] + list(map(int, input().split()))   # 돌의 초기 상태. 앞에 [-1]을 넣어 돌의 인덱스를 1부터 시작
    for _ in range(M):  # 뒤집기 작업 횟수 만큼
        i, j, w = map(int, input().split()) # 기준위치 i, 작업할 돌의 개수 j, 작업번호 w

        # 1번 작업
        if w == 1:
            for k in range(i, i+j):   # i 번째부터 j개의 돌을 뒤집기
                if 0 < k <= N:       # 범위 안에 있을 때
                    if arr[k] == 1:     # 뒤집기
                        arr[k] = 0
                    else:
                        arr[k] = 1

        # 2번 작업
        elif w == 2:                    # i 번째부터 j개의 돌을 i번째 색으로 바꾸기
            for l in range(i, i+j):
                if 0 < l <= N:          # 배열 안에서만 작업
                    arr[l] = arr[i]         # arr[l]에 arr[i]에 해당하는 값으로 바꾸기

        # 3번 작업
        elif w == 3:                    # i 번째를 기준으로 좌우 대칭일 경우 뒤집기
            for q in range(1, N):       # j가 4일때 1, 2 / 최대 범위를 N으로 넉넉히 잡고 if문으로 범위 제한
                cnt = 0
                left = i - q    # 왼쪽
                right = i + q   # 오른쪽
                # 만약 왼쪽이 0이상 n-1 미만이고 오른쪽이 3이상 N 이하이고 왼쪽과 오른쪽이 같고 돌을 뒤집은 횟수가 j가 아니라면
                if 0 < left < N-1 and 3 <= right <= N and arr[left] == arr[right] and cnt <= j:
                    # 왼쪽이 1일때
                    if arr[left] == 1:
                        cnt += 2        # 왼쪽 오른쪽 2개 뒤집어서 +2
                        arr[left] = 0
                        arr[right] = 0
                    # 왼쪽이 0일때
                    else:
                        cnt += 2
                        arr[left] = 1
                        arr[right] = 1

    print(f'#{tc}', *arr[1::])