import sys
input = sys.stdin.readline

n, m = map(int,input().split())

array1 = []
array2 = []

for _ in range(n):  
    array1.append(list(map(int, input().rstrip())))
for _ in range(n):
    array2.append(list(map(int, input().rstrip())))

count = 0

def change(a, b):
    for i in range(a, a + 3):
        for j in range(b, b+3):
            if array1[i][j] == 1 :
                array1[i][j] = 0
            else :
                array1[i][j] = 1

for i in range(n-2):
    for j in range(m-2):
        if array1[i][j] != array2[i][j]:
            change(i, j)
            count += 1

if array1 != array2 :
    count = -1

print(count)