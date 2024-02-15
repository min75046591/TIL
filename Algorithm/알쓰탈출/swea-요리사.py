"""
두명의 손님
N개의 식재료
식재료를 N/2해서 두개의 요리 = N * N 배열
각각의 음식을 A, B
맛의 차이 최소가 되도록 재료 분배

음식의 맛은 식재료들의 조합에 따라 다름
재료i는 j와 궁합이 잘 맞아 시너지 sij 발생

각 음식의 맛은 재료들의 시너지 sij들의 합

i와 j가 서로 같은 경우 sij는 없음, 0으로 주어짐

식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고, 
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 
그 최솟값을 정답으로 출력하는 프로그램을 작성하라.

A,B 요리의 값(위치의 대칭값) 차이의 최소값을 구하라

0으로 뚜껑을 씌워야 하나?
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    
    for i in range(N):
        food_sum = 0
        for j in range(N):
            food_sum = M
            A = 0
            B = 0
            food_sum += A - B