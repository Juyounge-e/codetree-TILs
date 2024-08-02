def cal(a,b):
    # 작은 수에 10을 더하기 
    if a > b:
        b += 10
        a *= 2
    else:
        a += 10
        b *= 2
    print(f'{a} {b}')

# 정수 a,b 입력 받기 
a,b = map(int, input().split())
cal(a,b)