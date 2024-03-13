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