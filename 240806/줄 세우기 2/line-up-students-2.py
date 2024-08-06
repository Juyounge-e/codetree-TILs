# n 
n = int(input())
# 키와 몸무게 정보 
info = []
for i in range(n):
    height, weight = map(int, input().split())
    info.append([height, weight, i+1])
    

# 키가 더 작은 학생이 앞으로, 키가 똑같 다면 무거운 학생이 뒤로 
info.sort(key = lambda x:(x[0], -x[1]))


for info in info:
    print(' '.join(map(str, info)))