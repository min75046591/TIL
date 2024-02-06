# 대각선 구하기 - 전치 행렬
'''
1. 5*5 2차 배열에 25개의 숫자를 저장
2. 대각선 원소의 합을 구하시오. 대각선 원소는 x자 위치의 원소를 나타냄
'''

# 입력 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0

for i in range(N):
    total += arr[i][i]  # 오른쪽 대각선 아래
    # 위에의 반대편 수 구하기
    total += arr[i][N-1-i] # 맨 끝은 인덱스가 4임으로 입력값 N에서 1을 뺌
                           # 그리고 i값만큼 빼줘서 i값 증가만큼 값을 내려줌
    # (2,2)위치가 2번 더해졌음으로 한번 빼줌
    total - arr[2][2]

print(total)


