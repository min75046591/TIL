"""
N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 이동

트럭 1개당 1개의 컨테이너 운반 가능. 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량.
A도시에서 B도시로 최대 M대의 트럭이 편도로 한 번만 운행

화물의 총 중향이 최대가 되도록 옮겼을때 화물의 전체 무게가 얼마인지

화물을 싣지 못한 트럭이나 남는 화물이 있을 수 있음.

컨테이너를 한 개도 옮길 수 없는 경우 0을 출력
"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # 컨테이너 수, 트럭 수
    w = list(map(int, input().split()))     # 컨테이너의 무게들
    t = list(map(int, input().split()))     # 트럭의 적재용량들
    tmp = []                                # 운반 가능한 컨테이너들을 모을 리스트
    w.sort(reverse=True)                    # 화물의 무게 오름차순
    t.sort(reverse=True)                    # 적재용량 오름차순

    i = j = 0
    while i < M and j < N:                  # 범위에 벗어나지 않을 때 동안
        if t[i] >= w[j]:                    # 적재용량이 컨테이너 무게보다 크거나 같을 때
            tmp.append(w[j])                # 컨테이너 무게 넣기
            i += 1
        j += 1                              # 적재용량이 컨테이너 무게보다 작을 땐 다음 컨테이너로 이동

    w.sort(reverse=True)    # 화물의 무게 오름차순
    t.sort(reverse=True)    # 적재용량 오름차순

    i = j = 0
    while i < M and j < N:
        if t[i] >= w[j]:
            tmp.append([w[j]])
            i += 1
        j += 1

    # 컨테이너들의 무게 합
    sum_v = 0
    for i in tmp:
        sum_v += i

    print(f'#{tc} {sum_v}')