# 19532

"""
1 3 -1 4 1 7
"""

A, B, C, D, E, F = map(int, input().split())

for x in range(-1000, 1001):
    for y in range(-1000, 1001):
        if A*x + B*y == C and D*x + E*y == F:
            print(x, y)
            break