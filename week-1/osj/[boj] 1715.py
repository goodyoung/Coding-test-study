import sys, heapq
input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0

while len(q) > 1 :
    sum = heapq.heappop(q) + heapq.heappop(q)
    result += sum

    heapq.heappush(q, sum)

print(result)