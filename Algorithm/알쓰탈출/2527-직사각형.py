"""
왼쪽 아래 (x,y)
오른쪽 위 (p,q)

직사각형	a
선분	b
점	c
공통부분이 없음	d
"""
square_map = [[0]*10000 for _ in range(10000)]
for _ in range(4):
    i1, j1, i2, j2, x1, y1, x2, y2 = map(int, input().split())
