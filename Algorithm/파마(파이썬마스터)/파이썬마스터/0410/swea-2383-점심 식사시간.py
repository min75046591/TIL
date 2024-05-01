"""
N*N 크기의 정사각형 모양의 방
사람들은 P
계단 입구 S
계단 입구까지 이동 시간  == |PR - SR| + |PC - SC|
PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치
== (사람 세로위치 - 계단 세로위치 )+ (사람 가로위치 - 계단 입구 가로위치)

계단을 내려가는 시간은 계단 입구에 도착한 후 부터 완전히 내려갈 때까지
입구에 도착하면 1분 후 아래칸으로 내려 갈 수 있음
계단 위에는 동시에 최대 3명
이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지
계단 입구에서 대기해야 함
계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K분이 걸림

모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 소요시간을 출력!

계단이 멀고 긴 곳의 사람을 기준으로 생각해보자
계단까지의 거리 + 계단 길이 + 1분
"""
import sys
sys.stdin = open('input.txt')
from collections import deque


def which_stair(level):     # 인간들이 향할 계단을 정하는 함수 (백트래킹)
    global min_v

    if level == cnt_people:     # 인간들이 어느 계단으로 향할 지 정해지면,
        going_down_stair(path)  # 내려보내보자
        return

    for k in range(2):  # 인간들은 0번 계단 또는 1번 계단으로 간다
        path.append(k)  # path에 0 또는 1 저장하고
        which_stair(level+1)   # 레벨 하나 올려서 재귀함
        path.pop(-1)


def going_down_stair(where_to_go):     # 인간들을 내려보내는 함수 - path를 인자로 받을 것임
    global min_v

    t = 0  # 시간을 나타낸다
    arrived = [deque(), deque()]  # 계단에 도착한 사람들을 저장
    going_down = [deque(), deque()]  # 계단을 내려가고 있는 사람들을 저장
    visited = [0] * cnt_people  # 계단에 각 사람이 도착했는지 안했는지
    cnt_finished = 0  # 계단을 내려간 사람의 수
    cnt_arrived = 0  # 계단에 도착한 사람의 수

    while cnt_finished < cnt_people:  # 계단을 인간들 전부 다 내려가지 않았으면 반복한다
        t += 1  # 시간 1 증가

        if min_v < t:  # 시간이 이미 구해진 최솟값보다 크면 그냥 리턴한다
            break

        for a in range(2):  # 계단 2개당
            while going_down[a]:  # 계단 내려가고 있는 사람이 있으면 먼저 내려간 사람부터 하나 빼낸다
                finished = going_down[a].popleft()
                if t == finished[1]:  # 지금 시간이 이 사람이 다 내려갈 시간이면 내보내고
                    cnt_finished += 1  # 계단 내려간 사람 수 증가
                else:  # 아직 다 못 내려간 사람이면 다시 넣어줌
                    going_down[a].appendleft(finished)
                    break

        for b in range(2):  # 계단 2개당
            while len(going_down[b]) < 3 and arrived[b]:  # 계단 내려가고 있는 사람이 3명보다 작고, 계단 도착한 사람 있으면
                arrived_person = arrived[b].popleft()  # 계단 먼저 도착한 사람부터 빼서
                arrived_person = [arrived_person, t + stairs[b][2]]  # 완료시간 = (현재시간 + 계단 내려가는데 걸리는 시간)을 저장하고
                going_down[b].append(arrived_person)  # 계단 내려가는 사람들에 넣는다.

        if cnt_arrived < cnt_people:  # 계단에 아직 모두 도달하지 못했다면,
            for m in range(cnt_people):  # 사람들 개수만큼 돌면서
                if not visited[m]:  # 각 사람이 계단 안내려갔으면
                    person = people[m]  # 각 사람
                    stair_num = where_to_go[m]  # path 에서 정해진 각 사람이 0, 1 중 내려갈 계단
                    if t >= times[person][stair_num]:  # 현재 시간이 각 사람이 해당 계단에 도착할 시간 이상이고,
                        if len(arrived[stair_num]) < 3:  # 계단에 도착한 사람이 3명보다 작으면,
                            arrived[stair_num].append(person)  # 계단 도착
                            visited[m] = 1  # 해당 사람은 계단에 도착함
                            cnt_arrived += 1  # 계단 도착한 사람 수 증가

    if min_v > t:  # 최솟값보다 완료된 시간이 작다면 최솟값 갱신
        min_v = t
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people = []     # 인간들을 저장
    stairs = []     # 계단들을 저장
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:
                people.append((i, j))
            elif tmp[j] > 1:
                stairs.append((i, j, tmp[j]))   # 계단의 값을 index 2에 저장한다
    cnt_people = len(people)    # 사람의 수 : 자주 사용하게 되어 저장

    times = {}  # 각 인간당 각 계단에 도달하는 시간(거리) 를 딕셔너리에 저장해둔다 (직접 이동하면 너무 빡셀 것 같아서)
    for each in people:
        time = []
        for stair in stairs:
            time.append(abs(each[0] - stair[0]) + abs(each[1] - stair[1]))
        times[each] = time

    path = []   # 인간들이 어느 계단으로 향할지 백트래킹으로 정하기 위함
    min_v = int(1e9)    # 최솟값 결과 저장할 변수
    which_stair(0) # 가즈아!!!!

    print(f'#{tc}', min_v)
