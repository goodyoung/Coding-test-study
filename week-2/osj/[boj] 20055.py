import sys 
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

belt = deque(map(int, input().split()))
robot = deque([0] * n)
result = 0

while True :
    belt.rotate(1)
    robot.rotate(1)

    robot[-1] = 0

    for i in range(n-2, -1, -1):
        if robot[i+1] == 0 and robot[i] == 1 and belt[i+1] > 0 :
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[-1] = 0

    if belt[0] > 0 :
        robot[0] = 1
        belt[0] -= 1
    
    result += 1

    if belt.count(0) >= k :
        break

print(result)

    