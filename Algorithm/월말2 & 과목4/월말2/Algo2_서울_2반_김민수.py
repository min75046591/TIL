"""
사격 게임
게임 단계에 따라 3x3에서 8x8 규격의 표적
가로 한 줄에서 한 개의 표적을 선택 가능
세로 한 줄에서 한 개의 표적 선택 가능
-> 세로와 가로에 곂치면 안됌

한 줄에서 2개 이상의 표적을 맞추면 그 단계는 실격

어떤 단계에는 표적 한 개의 점수가 음수로 나타남. 이 표적을 맞추면 그 단계는 실격

"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            # 음수를 맞췄을 때
            if arr[i][j] == -1:
                max_v = 0
                break
            # 양수만 맞췄을 때
            else:
            # 각 점수별로 i와 j가 같으면 안됌 -> N만큼 표적 맞추기
            for k in range(N):
                if