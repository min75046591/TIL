"""
성별이 같고 학년이 같아야함
최대 인원 = K
모든 학생을 배정하기 위해 필요한 방의 최소 개수
여자 : 0
남자 : 1
"""
N, K = map(int, input().split())
stu = [list(input().split()) for _ in range(N)]
cnt = [0]*(K*6)
for i in range(N):
    if stu[i]


