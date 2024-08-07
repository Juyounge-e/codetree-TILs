# a진수로 표현된 n을 b진수 n으로 바꾸기 
def change_base(a, b, n):
    # n을 10 진수로 바꾸기 
    demical_num = int(n, a)

    # 10진수로 바꾼 n을 b진수 n으로 바꾸기 
    digits = [] # 배열에 mod값을 저장 
    if demical_num == 0:
        return '0'

    while demical_num > 0:
        digits.append(demical_num % b)
        demical_num //= b
    
    digits.reverse()
    result = "".join(map(str, digits))
    
    return result 

# a,b 입력 
a, b = map(int, input().split())
n = input()

print(change_base(a,b,n))