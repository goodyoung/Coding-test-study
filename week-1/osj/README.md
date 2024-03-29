## 2141 - 우체국

골드 4

[문제 링크](https://www.acmicpc.net/problem/2141)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bboj%5D%202141.py)

### 핵심 아이디어
모든 마을 사람의 총합의 절반을 넘어가는 순간의 마을이 정답

</br>

입력 단계에서 모든 사람의 수를 계산하고 

마을을 순서대로 정렬하기 위해 array.sort(key = lambda x : x[0]) 로 정렬한다.

마을의 사람 수를 카운트하면서 전체 사람의 절반을 넘어간 순간의 마을을 찾는다.

</br>

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

</br>

문제를 봤을 때, 제한 시간에 비해 입력 값이 작은 것을 알 수 있다.

단순하게 같은 위치의 값이 다르면 3x3의 행렬의 모든 값을 바꿔준다.

</br>

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

</br>

강의 시간이 겹치면 우선순위 큐에 강의 종료 시간을 push한다. 

우선순위 큐의 최소값보다 강의 시작 시간이 빠르다면 무조건 다른 강의 실을 써야하므로 push, 

느리다면 우선순위 큐의 값을 pop하고 강의 종료 시간을 push한다.

</br>

리스트를 사용하여 같은 강의실을 쓰는 강의를 삭제시키며 카운트하는 풀이를 먼저 생각했다. 

루프의 제한선을 계산하는 과정에서 에러가 났고 수정하기 힘들다고 생각했다.

다음으로 우선순위 큐를 이용해야겠다고 생각했지만 위의 사고 과정에서 벗어나지 못해 풀이를 떠올리지 못했다.

heapq 사용에 익숙해지고 많은 문제를 풀어야겠다.

---

## 프로그래머스 42883 - 큰수 만들기

레벨 2

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42883)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bprogrammers%5D%2042883.py)

### 핵심 아이디어

결과의 첫 숫자는 앞에서부터 k자리까지의 숫자 중 가장 큰 수가 와야한다. 

ex) number = 238901, k = 5 이면, 앞에서부터 5자리까지의 숫자(23890) 중 가장 큰 수(9) 가 와야한다

<br>

맨 앞자리가 결정되었으니 필요없는 숫자는 제거하고 남은 k 값을 계산하여 두번째 자리부터 같은 방식을 반복한다.

<br>

결국 큰 수가 되기 위해선 맨 앞 자리가 가장 큰 수가 되어야 한다고 생각한 이후로는 문제를 금방 풀었다.

처음에는 문자열을 리스트로 바꾸고 값을 삭제시키려 했는데 백준 11000 문제에서 같은 방식으로 풀려다가

실패했던 경험을 떠올리고 새로운 리스트에 값을 저장하는 방법으로 문제를 풀었다.

<br>

문제를 풀고 다른 사람의 풀이를 봤다. 로직은 같은데 훨씬 간결하게 작성된게 눈에 보였다.

좀 더 간결하게, 한 번에 처리할 수 있는 것은 한 번에 작성할 수 있도록 노력해야겠다.

---

## 2839 - 설탕 배달

실버 4

[문제 링크](https://www.acmicpc.net/problem/2839)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bboj%5D%202839.py)

### 핵심 아이디어

5로 나누는 개수를 늘려가며 나머지 값을 3으로 나눈다.

---

## 1715 - 카드 정렬하기

골드 4

[문제 링크](https://www.acmicpc.net/problem/1715)

[풀이](https://github.com/ooosj/Coding-test-study/blob/main/week-1/osj/%5Bboj%5D%201715.py)

### 핵심 아이디어

가장 작은 묶음을 더해준다. 새로 만든 묶음을 다시 큐에 넣는다.

<br>

입력 값의 크기가 10만이기때문에 O(nlogn) 의 시간 복잡도를 갖도록 작성해야한다.

시간을 줄이기 위해서 우선순위큐를 사용하여 요소를 삽입 삭제한다.

