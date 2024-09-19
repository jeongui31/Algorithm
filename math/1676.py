from math import factorial

N = int(input())
zero = 0

for char in str(factorial(N))[::-1]:
    if char == '0':
        zero += 1
    else:
        break
        
print(zero)