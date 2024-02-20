"""
- 문제 -
첫 번째는 무조건 0번
다음은 0 or 1
세 번째는 0, 1, 2중 하나의 번호
각자 뽑은 번호는 자신이 처음에 선 순서보다 작은 수
0은 제자리. 그 외 번호는 뽑은 만큼 앞자리로 이동
학생들이 최종적으로 줄을 선 순서를 출력

-입력 -
1. 학생의 수
2. 줄을 선 차례대로 학생들이 뽑은 번호
학생 수 >= 100 , 뽑는 번호는 0 or 자연수
뽑은 번호 사이에는 빈 칸이 하나씩 있음

-출력-
학생들이 처음에 줄을 선 순서대로 1번부터 번호.
첫째 줄에 학생들이 최종적으로 줄을 선 순서를 그 번호로 출력
학생 번호 사이에는 한 칸의 공백을 출력

input
5
0 1 1 3 2

output
4 2 5 3 1
"""
def line_up(N, pick_num_list, arr):
    for i in range(2, N+1):  # 사람 순서 -> 1번째는 고정이라 2번째 사람부터
        if pick_num_list[i-1] == 0:
            arr.append(i)   # 사람 번호와 인덱스 번호를 인덱스 번호로 변환
        elif pick_num_list[i-1] > 0:
            arr.insert(i-1, i)       # 0 보다 큰 숫자를 뽑으면 그 숫자만큼 앞으로
    return arr

N = int(input())
pick_num_li = list(map(int, input().split()))
arr = []   # 순서를 저장할 배열[0,0,0,0,0]
arr.append(1)   # 첫 번째 사람은 고정
arr = line_up(N, pick_num_li, arr)
print(*reversed(arr))