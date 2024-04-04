import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

ladder = {}
snake = {}

board = [0] * 101

visited = [False] * 101

for _ in range(n):
  x, y = map(int, sys.stdin.readline().strip().split())
  ladder[x] = y
    
for _ in range(m):
  x, y = map(int, sys.stdin.readline().strip().split())
  snake[x] = y

q = deque([1])

while q:
    x = q.popleft()

    if x == 100 :
        print(board[x])
        break

    for d in range(1,7):
        next = x + d

        if next <= 100 and not visited[next]:
            if next in ladder.keys():
                next = ladder[next]
            if next in snake.keys():
                next = snake[next]

            if not visited[next]:
                visited[next] = True
                board[next] = board[x] + 1
                q.append(next)

            