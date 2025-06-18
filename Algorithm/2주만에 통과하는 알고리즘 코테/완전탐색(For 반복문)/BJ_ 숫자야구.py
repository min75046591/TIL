# 2503

"""
4
123 1 1
356 1 0
327 2 0
489 0 1
"""

n = int(input())

numbers = [list(map(str,input().split())) for _ in range(n)]
# string을 미리 넣어준 이유는, 나중에 쪼개기 위해서

answer = 0

# (1) 세 자리 숫자 만들기
for a in range(1,10): # 100의 자리수
    for b in range(1,10): # 10의 자리수
        for c in range(1,10): # 1의 자리수
            counter = 0
            
            # (2) 다른 세 자리수
            if( a == b or b == c or c == a):
                continue

            # (3) 배열에 넣은 조건을 넣어주기
            for array in numbers:
                check = list(array[0]) # ['1','2','3']
                strike = int(array[1])
                ball = int(array[2])

                strike_count = 0
                ball_count = 0

                #스트라이크 계산기
                if (a == int(check[0])):
                    strike_count += 1
                if (b == int(check[1])):
                    strike_count += 1
                if (c == int(check[2])):
                    strike_count += 1
                

                #볼 계산기
                if (a == int(check[1]) or a == int(check[2])):
                    ball_count += 1
                if (b == int(check[0]) or b == int(check[2])):
                    ball_count += 1
                if (c == int(check[0]) or c == int(check[1])):
                    ball_count += 1
                
                
                #(4) 매칭 여부 확인하기
                if (strike != strike_count):
                    break
                if (ball != ball_count):
                    break
                
                counter += 1

            if counter == n:
                answer += 1
                
print(answer)
