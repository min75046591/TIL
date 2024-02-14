"""
성별이 같고 학년이 같아야함
한 방당 최대 인원 = K
학생 수 = N
모든 학생을 배정하기 위해 필요한 방의 최소 개수
여자 : 0
남자 : 1
"""
import math

N, K = map(int, input().split())
room = 0
student_li = [0] * 13
for i in range(N):    # 학생들    
    gender, grade = map(int, input().split())
    if gender == 0:
        student_li[grade] += 1  # 남학생은 1~6 인덱스
    if gender == 1:   # 여학생은 7~12 인덱스
        student_li[grade + 6] += 1

for stu in student_li:
    room += math.ceil(stu/K)
print(room)