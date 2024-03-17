import sys
input = sys.stdin.readline

n = int(input())

result = 1e10

for i in range(n//5+1):
    m = n - (5*i)
    
    if m % 3 == 0 :
        sum = m // 3 + i
        result = min(sum, result)

if result == 1e10:
    print(-1)
else :
    print(result)