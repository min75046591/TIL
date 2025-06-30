## 문제
![Image](https://github.com/user-attachments/assets/71c6d57f-50f1-4573-8cfd-09debc7d266e)

![Image](https://github.com/user-attachments/assets/7e9aa80d-5d64-4d13-b6ed-efb616dc2d2a)

![Image](https://github.com/user-attachments/assets/762b565f-65bd-429b-95a4-963fd704bd72)

## python

```python
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2

    if total % 2 != 0:
        return -1  # 절대 같아질 수 없음

    target = total // 2
    cnt = 0
    limit = len(q1) * 3  # 최악의 경우를 막기 위한 안전 장치

    while cnt <= limit:
        if sum1 == target:
            return cnt
        elif sum1 > target:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum2 -= x
            sum1 += x
        cnt += 1

    return -1

```

## JS

```javascript
function solution(queue1, queue2) {
    var answer = -2;
    
    const q1 = [...queue1]
    const q2 = [...queue2 ]
    let sum1 = q1.reduce((acc, cur) => acc + cur, 0)
    let sum2 = q2.reduce((acc, cur) => acc + cur, 0)
    const total = sum1 + sum2
     
    // 총합이 홀수면 절대 절반으로 나눌 수 없기 때문에 -1 반환
    if (total % 2 !== 0) return -1
    
    const target = total / 2    // 목표 합
    const limit = queue1.length * 3 // 무한 루프 방지를 위한 제한
    
    let cnt = 0
    let p1 = 0
    let p2 = 0
    
    while (cnt <= limit) {
        if (sum1 === target) return cnt
        
        if (sum1 > target) {
            const x = q1[p1++]
            sum1 -= x
            sum2 += x
            q2.push(x)  // q2 뒤에 추가
        } else {
            // q2의 앞에서 하나 빼서 q1로 이동
            const x = q2[p2++]
            sum2 -= x
            sum1 += x
            q1.push(x)  // q1 뒤에 추가
        }
        cnt++   // 이동 횟수 증가
        
    }
    // 반복해도 못맞추면 -1 반환
    return -1;
}
```

### 사용된 문법과 개념

| 문법/개념                                | 설명                                                                 |
| ------------------------------------ | ------------------------------------------------------------------ |
| `...queue1`                          | 배열을 **얕은 복사**해서 새로운 배열을 만듦.<br>원본 데이터를 보존하면서 수정하려고 할 때 사용          |
| `reduce((acc, cur) => acc + cur, 0)` | 배열 요소의 누적 합을 계산할 때 사용.<br>`acc`는 누적값, `cur`는 현재 요소                 |
| `q1[p1++]`                           | 큐에서 `shift()`를 하지 않고, **앞 포인터만 증가시키며** 앞에서 제거하는 것처럼 처리. 성능상 훨씬 효율적 |
| `q1.push(x)`                         | 큐의 뒤쪽에 요소 추가 (큐의 enqueue 동작)                                       |
| `cnt <= limit`                       | 큐에서 무한 루프가 발생하지 않도록 제한을 설정. 최악의 경우를 기준으로 `3 * n` 정도로 잡음            |
| `sum1 === target`                    | 두 큐가 동일한 합이 되는 조건을 만족할 때 루프 종료                                     |
