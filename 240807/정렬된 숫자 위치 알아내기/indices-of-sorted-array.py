'''# n 입력 
n = int(input())
# 크기가 n인 수열 입력 
arr = list(map(int, input().split()))

# 오름차순으로 정렬
arr2 = sorted(arr) # 기존 배열은 유지하고 새롭게 저장 

# 각 위치에 있던 원소가 어디로 이동했는지 출력하기 
new = [] # 출력 값을 저장할 배열 
for i in range(n):
    changed_idx = arr2.index(arr[i]) 
    new.append(changed_idx+1)

print(new)
# 같은 값의 원소를 가지면 어떻게 해결해야할지 모르겠음 
# 클래스로 사용하는 이유도 알아보기 '''

# n 입력 
n = int(input())
# 크기가 n인 배열 입력 
arr = list(map(int, input().split()))

numbers = [(num,i) for i, num in enumerate(arr)] # 수, 인덱스로 배열 보정 
answer = [0 for _ in range(n)] # 정답 배열 초기화 

number.sort(key = lambda x:(x[0], x[1]))

for i, (num, idx) in enumerate(numbers):
    answer[index] = i +1 # 인덱스 보정 

print(" ".join(map(int, answer)))