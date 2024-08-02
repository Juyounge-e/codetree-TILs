# n, m 입력
n, m = map(int, input().split())
# n개의 원소 수열 A입력 
global arr 
arr = list(map(int, input().split()))
# 2개의 숫자쌍 m번 입력 
mylists = []
for _ in range(m):
    mylists.append(list(map(int, input().split())))

for mylist in mylists:
    a1, a2 = mylist
    print(sum(arr[a1-1:a2]))



'''
print(n, m)
print(arr)
print(mylist)
'''