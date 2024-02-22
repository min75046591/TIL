import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a, b = map(int, input().split())

print(a+b)
print(a*b)

