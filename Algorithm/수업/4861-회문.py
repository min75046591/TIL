T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 문장 개수와 길이 / M은 부분적으로 조사할 길이
    arr = [input() for _ in range(N)]
    result = ''
# 가로 탐색
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j: j+M] == arr[i][j: j+M][::-1]: #  i 행에서 j부터 j+M 까지의 부분 문자열이 뒤집은것과 같다면
                result = arr[i][j : j+M]
                break  # for j  -> 11~14열은 선생님이 수정해줌
        else:
            continue  # for j
        break

# 세로 탐색
    for i in range(N-M+1):
        for j in range(N):
            # 세로축만 모은 단어 생성
            vertical = ''
            for x in range(i, i+M):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                result = vertical

    print(f'#{tc} {result}')












    # tmp = []
    # for word in arr:
    #     for j in range(N):
    #         if word[j] == word[M - 1 - j]:
    #             tmp.append(word)
    #     else:
    #         continue
    # print(f'#{tc} {tmp}')