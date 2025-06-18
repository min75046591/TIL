# 14568

"""
6
"""

candy = int(input())

cnt = 0
for A in range(0, candy+1): # 0 ~ 6개
    for B in range(0, candy+1): # 0 ~ 6개
        for C in range(0, candy+1): # 0 ~ 6개
            if  A + B + C == candy:
                if A >= B+2:
                    if A > 0 and B > 0 and C > 0:
                        if C % 2 == 0:
                            cnt += 1
print(cnt)