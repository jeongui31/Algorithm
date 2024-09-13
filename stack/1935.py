N = int(input())
equ = input()
ope = [int(input()) for _ in range(N)]
stack = []

for i in equ:
    if i.isalpha():
        stack.append(ope[ord(i)-ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if i == '+':
            stack.append(n1+n2)
        elif i=='-':
            stack.append(n1-n2)
        elif i=='/':
            stack.append(n1/n2)
        elif i=='*':
            stack.append(n1*n2)
            
print("{:.2f}".format(*stack))