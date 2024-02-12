T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001  # 5000번 정류장
    #N개의 노선을 정류장에 표시
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):  # 1<=A<=B<=5000  -> A이상 B이하
            counts[j] += 1  # 버스가 지나가는 곳에 1씩 추가
    p = int(input())
    busstop = [int(input()) for _ in range(p)]
    print(f'#{tc}', end = ' ')
    for i in busstop:   # 출력할 정류장
        print(counts[i], end = ' ')
    print()