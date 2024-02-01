T = int(input())
for tc in range(1, T+1):
    p, pa, pb = map(int, input().split()) # 전체 쪽 수:P, A, B가 찾을 쪽 번호
    l, r = 1, 400
    c = int((l+r)/2)

    def binary_search(p,result_page):
        start = l
        end = r
        cnt = 0
        while start <= end:
            middle = c




