import sys, heapq
input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

array.sort()

heap = []
heapq.heappush(heap, array[0][1])

for i in range(1,n):
    if array[i][0] < heap[0]:
        heapq.heappush(heap, array[i][1])
    else :
        heapq.heappop(heap)
        heapq.heappush(heap, array[i][1])

print(len(heap))
