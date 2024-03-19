"""
0시부터 다음날 0시(24시까지)까지 A도크 사용신청을 확인해서 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록
최대 몇 대의 화물차가 이용할 수 있는지

작업 시작 시간과 완료 시간이 매시 정각 기준으로 표시
앞 작업의 종료와 동시에 작업을 시작할 수 있다.

종료 시간과 시작 시간 비교
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort()
    time.sort(key=lambda x:x[1])
    cnt = 1
    end = time[0][1]

    for i in range(1, N):
        if end <= time[i][0]:
            end = time[i][1]
            cnt += 1
    print(f'#{tc} {cnt}')
