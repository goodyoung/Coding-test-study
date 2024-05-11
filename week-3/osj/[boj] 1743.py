import sys
from collections import deque

n, m, k = map(int,input().split())

graph = [[0] * (m + 1) for _ in range(n+1)]

q = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(k):
    a, b = map(int,input().split())
    graph[a][b] = 1

def bfs(x, y):
    graph[x][y] = 2

    q.append([x,y])

    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx < n+1 and 0 <= ny < m+1 and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append([nx, ny])
                count += 1

    return count

result = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1 :
            result = max(result, bfs(i, j))

print(result)