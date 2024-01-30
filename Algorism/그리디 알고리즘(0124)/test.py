# 입력값 받기
T = int(input())  # 테스트 케이스의 수
N = int(input())  # 양수의 개수
ai = map(int, input().split()) # 양수 입력값

# 데이터 넣을 곳
data = [ai]  # 입력받은 데이터
counts = [0] * (N+1) # 카운트 배열
temp = [0] * N  # 정렬된 데이터를 넣을 곳

# counts 배열에 기록하기 -> 같은 숫자들 개수 파악
for j in data:
    counts[j] += 1

# counts 누적합 구하기
for i in range(1, N+1):
    counts[i] = counts[i-1] + counts[i]

# data의 마지막 원소부터 정렬 시작
for i in range(N-1, -1, -1):
    counts[data[i]] -= 1
    temp[counts[data[i]]] = data[i]

print(*temp)