"""
이동경로가 겹치지 않으면 1초만에 도착
따라서 가장 많이 겹치는 구간의 값을 구하면 됨!

특징 1 왼쪽에서 오른쪽으로 이동한다고 통일
목적지 > 출발지
swap을 사용

특징 2 아랫방 사람들을 모두 윗방으로 이주 -> 정답 결과는 어차피 같음
if 짝수:
    s -= 1
    e -= 1

사람들이 지나간 경로에 1을 추가
"""
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())    # 돌아가야 할 학생들의 수
#     arr = [0] * 401     # 복도 리스트
#     max_v = 0             # 총 걸린 시간
#     for _ in range(N):
#         # s 출발 방, e 도착 방
#         s, e = map(int, input().split())
#
#         # 특징 2. 아랫방을 윗방으로 이동
#         if s % 2 == 0: s -= 1
#         if e % 2 == 0: e -= 1
#
#         # 특징 1전 출발점보다 목적지가 더 큰 값이 되도록 swap
#         if s > e: s, e = e, s
#
#         for i in range(s, e+1):
#             arr[i] += 1
#             max_v = max(arr[i], max_v)
#             # if max_v < arr[i]
#             #    max_v = arr[i]
#         print(f'#{tc} {max_v}')

"""
가장 많이 겹치는 구간의 값을 찾으면 된다
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 돌아가야 할 학생들의 수
    arr = [0] * 400
    for _ in range(N):
        start, end = map(int, input().split())
    # 방을 한줄로 만들기
        if start % 2 == 0:
            start = start - 1
        if end % 2 == 0:
            end = end - 1
    # start 가 end 보다 작도록 바꿔주기
        if start > end:
            start, end = end, start

        for i in range(start, end+1):
            arr[i] += 1
    result = max(arr)
    print(f'#{tc} {result}')