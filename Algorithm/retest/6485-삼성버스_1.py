T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0]*5001

    for i in range(N):
        A, B = map(int, input().split()) # A와 B가 다니는 정류장 값을 받음
        for j in range(A, B+1):  # A정류장부터 B정류장까지의 범위
            counts[j] += 1      # 첫번째 노선 1~3 정류장 / 두번째 노선 2~5정류장에 1씩 더하기
    P = int(input())
    busstop = [int(input()) for _ in range(P)]    # p만큼 돌면서 입력을 받음
    print(f'#{tc}', end = ' ')  # 한 줄에 p개의 정수를 공백 하나로 구분하여 출력
    for i in busstop:
        print(counts[i], end = ' ')
    print()



