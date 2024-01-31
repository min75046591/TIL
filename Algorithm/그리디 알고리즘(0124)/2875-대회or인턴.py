# 대회 = 여학생2명 & 남학생1명
    # 대회에 참여하려는 학생들 중 k명은 인턴쉽
    # 인턴쉽 참여하는 학생은 대회 참여 x
    # 최대의 팀 수
# 여학생 : N / 남학생 : M / 인턴쉽 : K

n, m, k = map(int, input().split())

def cal_max_teams(n, m, k):
    max_teams = min(n//2, m, (n+m-k//3))
    return max_teams

result = cal_max_teams(n, m, k)

print(result)