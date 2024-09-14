S = input()
alpha = [-1]*26

for s in S:
    alpha[ord(s)-ord('a')] = S.index(s)
    
print(*alpha)