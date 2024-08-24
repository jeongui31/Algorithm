T = int(input())

for _ in range(T):
    s = input()
    stack=[]    
    for w in s :
        if w == '(':
            stack.append(w)
        elif w == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else :
        if not stack:
            print('YES')
        else:
            print('NO')