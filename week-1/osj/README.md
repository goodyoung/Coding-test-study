## 2141 - 우체국

골드 4

[문제 링크](https://www.acmicpc.net/problem/2141)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bboj%5D%202141.py)

### 핵심 아이디어
모든 마을 사람의 총합의 절반을 넘어가는 순간의 마을이 정답

---

입력 단계에서 모든 사람의 수를 계산하고 

마을을 순서대로 정렬하기 위해 array.sort(key = lambda x : x[0]) 로 정렬한다.

마을의 사람 수를 카운트하면서 전체 사람의 절반을 넘어간 순간의 마을을 찾는다.

---

단순하게 마을 하나하나 우체국을 세워 값을 계산하면 O(n^2)의 시간 복잡도가 나와 시간초과가 난다.

그리디 문제 중 중앙값을 이용할 수 있을 것 같은 문제는 중앙값을 이용해 풀이하는 방법을 생각해보면 좋을 것 같다

증명 :
https://math.stackexchange.com/questions/4410205/minimum-value-of-sum-of-absolute-diferences

---

## 1080 - 행렬
실버 1

[문제 링크](https://www.acmicpc.net/problem/1080)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bboj%5D%201080.py)



### 핵심 아이디어

그냥 하나하나 다 비교하기

---

문제를 봤을 때, 제한 시간에 비해 입력 값이 작은 것을 알 수 있다.

단순하게 같은 위치의 값이 다르면 3x3의 행렬의 모든 값을 바꿔준다.

---

문제의 제한 시간을 잘 파악하고 문제 풀이를 생각하면 좋을 것 같다.

또 문제를 풀면서 가독성을 높이기 위해 함수를 만들어 문제를 푸는 방법도 좋은 것 같다.

---

## 11000 - 강의실 배정

골드 5

[문제 링크](https://www.acmicpc.net/problem/11000)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bboj%5D%2011000.py)

### 핵심 아이디어

우선순위 큐를 이용한다.

heap의 노드가 강의실 하나를 사용하는 형태를 만든다.

---

강의 시간이 겹치면 우선순위 큐에 강의 종료 시간을 push한다. 

우선순위 큐의 최소값보다 강의 시작 시간이 빠르다면 무조건 다른 강의 실을 써야하므로 push, 느리다면 우선순위 큐의 값을 pop하고 강의 종료 시간을 push한다.

---

리스트를 사용하여 같은 강의실을 쓰는 강의를 삭제시키며 카운트하는 풀이를 먼저 생각했다. 루프의 제한선을 계산하는 과정에서 에러가 났다

다음으로 우선순위 큐를 이용해야겠다고 생각했지만 위의 사고 과정에서 벗어나지 못해 풀이를 떠올리지 못했다.

heapq 사용에 익숙해지고 많은 문제를 풀어야겠다.

