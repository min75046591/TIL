'''
N * N = 파리 맵 리스트 
M * M = 파리채 크기

파리채로 내리 쳤을 때 가장 많은 파리를 잡을 수 있는 파리의 수를 구하라
'''

T = int(input())  # 테스트 케이스 입력값
for tc in range(1, T+1):
    M, N = map(int, input().split())    # 맵 크기와 파리채 크기

    fly_map = [map(int, input().split()) for _ in range(M)]     # 
    kill_list = []  # 파리채로 잡은 파리들의 수 넣기

    for i in range(M-N+1):
        for j in range(M-N+1):
            sum_num = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    sum_num += fly_map[k][l]
                    kill_list.append(sum_num)
    
    max_v = 0
    for x in kill_list:
        if max_v < x:
            max_v = x

    print(f'#{tc} {max_v}')