import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())

array = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

result = 0

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            queue.append([i,j])

def bfs(array):
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append([nx,ny])


bfs(array)

for i in array:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result - 1)