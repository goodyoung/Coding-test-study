### 2141 - 우체국

골드 4

문제 링크 : https://www.acmicpc.net/problem/2141

```
import sys
input = sys.stdin.readline

n = int(input())

array = []
people = 0

for _ in range(n):
    q, w = map(int,input().split())
    array.append([q,w])
    people += w

array.sort(key = lambda x : x[0])

count = 0

for i in range(n):
    count += array[i][1]
    if count >= people/2 :
        print(array[i][0])
        break
```

#### 핵심 아이디어
모든 마을 사람의 총합의 절반을 넘어가는 순간의 마을이 정답

---

단순하게 마을 하나하나 우체국을 세워 값을 계산하면 O(n^2)의 시간 복잡도가 나와 시간초과가 난다.

그리디 문제 중 중앙값을 이용할 수 있을 것 같은 문제는 중앙값을 이용해 풀이하는 방법을 생각해보면 좋을 것 같다

증명 :
https://math.stackexchange.com/questions/4410205/minimum-value-of-sum-of-absolute-diferences