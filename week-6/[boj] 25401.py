import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

pair = set()

for i in range(n-1):
    for j in range(i+1,n):
        a = (arr[i] - arr[j]) / (i - j)
        if a - int(a) == 0:
            b = arr[j] - a * j # a가 정해졌을 때 나오는 b
            pair.add((a, b))
        
change_list = []

for (a, b) in pair: # 가능한 모든 (a, b) 쌍으로 그래프를 만들고 카드를 대입
    change = 0
    for l in range(n):
        if arr[l] != a * l + b:
            change += 1
    change_list.append(change)
    
print(min(change_list))