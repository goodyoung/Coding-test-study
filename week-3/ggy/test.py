import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for i in arr:
    i.sort()
    
def dfs(num):
    for i in arr[num]:
        if not visited[i]:
        
            # for i in arr[num]:
            visited[i] = 1
            print(i, end = ' ')
            dfs(i)
            
            
def bfs(num):
    q = deque()
    q.append(num)
    print()
    print(num, end=' ')
    while q:
        x = q.popleft()
        visited[x] = 1        
        for i in arr[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                print(i, end=' ')
                
visited=[0]*(N+1)
print(V, end= ' ')
visited[V] = 1
dfs(V)
visited=[0]*(N+1)
bfs(V)