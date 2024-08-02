# 정수 n 입력 
n = int(input())

def star(n):
    print('* ' * n)

for i in range(n, 0, -1):
    star(i)
for j in range(1, n+1):
    star(j)