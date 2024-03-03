"""
키의 합이 100
난쟁이는 9명 그 중 진짜는 7명
오름차순으로 출력
"""
arr = [int(input()) for _ in range(9)]
arr.sort()
for a in range(3):
    for b in range(a+1, 4):
        for c in range(b+1, 5):
            for d in range(c+1, 6):
                for e in range(d+1, 7):
                    for f in range(e+1, 8):
                        for g in range(f+1, 9):
                            if arr[a]+ arr[b] + arr[c] + arr[d] + arr[e] + arr[f] + arr[g] == 100:
                                result = arr[a], arr[b], arr[c], arr[d], arr[e], arr[f], arr[g]

for i in result:
    print(i, end='\n')
