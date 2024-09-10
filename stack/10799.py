stack = []
stick = 0

cmd = list(input())

for i in range(len(cmd)) :
    if cmd[i] == '(':
        stick += 1
        stack.append(cmd[i])
    elif cmd[i] == ')':
        if cmd[i-1] == '(':
            stick -= 1
            stack.pop()
            stick += len(stack)
        else:
            stack.pop()
            
print(stick)