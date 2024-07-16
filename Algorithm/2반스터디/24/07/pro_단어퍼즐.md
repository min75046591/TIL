# 단어 퍼즐
## 생각한 풀이
- dfs로 조합을 만들어서 최솟값 도출
- 아니면 dp
- gpt의 도움을 받음. dp값 갱신 부분을 생각하지 못함
- float('inf') : 무한대


```python
def solution(strs, t):
    # 목표 단어 길이 + 1 만큼 dp 배열 생성 (무한대로 초기화)
    dp = [float('inf')] * (len(t) + 1)
    dp[0] = 0  # 빈 문자열을 완성하는 데 필요한 조각 수는 0

    # 목표 단어의 각 위치에 대해
    for i in range(1, len(t) + 1):
        # 모든 부분 문자열 검사
        for j in range(i):
            # 부분 문자열이 strs에 포함되어 있는지 확인
            if t[j:i] in strs:
                # dp 값을 갱신
                dp[i] = min(dp[i], dp[j] + 1)
    
    # 목표 단어를 완성할 수 없는 경우 -1 반환
    return dp[-1] if dp[-1] != float('inf') else -1

```

### dfs로 푸는법 

채점 결과
정확성: 46.9
효율성: 0.0
합계: 46.9 / 100.0

```python
def solution(strs, t):
    # 메모이제이션을 위한 딕셔너리
    memo = {}  

    def dfs(index):
        # 목표 단어의 끝에 도달한 경우 (완성된 경우)
        if index == len(t):  
            return 0

        # 이미 계산된 결과가 있으면 메모이제이션 값 반환
        if index in memo:  
            return memo[index]

        # 최소 조각 수를 무한대로 초기화 (최소값을 찾기 위해)
        min_pieces = float('inf')  

        # 현재 위치부터 목표 단어의 끝까지 모든 부분 문자열 검사
        for end in range(index + 1, len(t) + 1):
            # 부분 문자열이 단어 조각들에 포함되어 있는지 확인
            if t[index:end] in strs:
                # 부분 문자열의 끝에서부터 다시 dfs 호출
                result = dfs(end)
                # 유효한 경로인 경우 최소값 갱신
                if result != float('inf'):
                    min_pieces = min(min_pieces, result + 1)

        # 메모이제이션에 최소 조각 수 저장
        memo[index] = min_pieces  
        return memo[index]

    # dfs 함수 호출, 결과가 무한대이면 -1 반환
    result = dfs(0)
    return result if result != float('inf') else -1
```

### 코드 설명

1. 메모이제이션 딕셔너리(memo) 생성:
- 이미 계산된 결과를 저장하여 중복 계산을 방지합니다.

2. DFS 함수 정의(dfs):

- index는 현재 목표 단어 t에서 탐색을 시작할 위치를 나타냅니다.
- index가 t의 길이와 같아지면 (즉, 목표 단어를 완성한 경우) 0을 반환합니다.
- index가 memo에 존재하면, 이미 계산된 결과를 반환합니다.
- min_pieces를 float('inf')로 초기화하여 최소값을 찾기 위한 기준값으로    설정합니다.
index부터 목표 단어의 끝까지 모든 부분 문자열을 검사합니다. 부분 문자열이 strs에 포함되어 있다면, 그 끝에서부터 다시 DFS를 호출하여 최소 조각 수를 계산합니다.
각 호출 결과를 비교하여 min_pieces를 갱신합니다.
계산된 최소 조각 수를 memo에 저장합니다.
DFS 호출 및 결과 반환:

dfs(0)을 호출하여 목표 단어 전체에 대한 최소 조각 수를 계산합니다.
결과가 무한대이면 (즉, 목표 단어를 완성할 수 없는 경우) -1을 반환합니다.
주요 아이디어
DFS: 모든 가능한 경로를 탐색하여 목표 단어를 완성하는 데 필요한 최소 조각 수를 찾습니다.
메모이제이션: 이미 계산된 경로의 결과를 저장하여 중복 계산을 방지하고, 효율성을 높입니다.
부분 문자열 검사: 목표 단어의 각 위치에서 가능한 모든 부분 문자열을 검사하여 유효한 조각을 찾습니다.