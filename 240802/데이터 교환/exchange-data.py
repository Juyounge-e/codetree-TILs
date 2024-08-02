a, b, c = 5, 6, 7 

temp = a
a = c
c = b 
b = temp 
print(f'{a}\n{b}\n{c}')