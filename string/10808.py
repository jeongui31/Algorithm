S = input()
alpha = [0]*26

for s in S :
    alpha[ord(s)-ord('a')] += 1
    
print(*alpha)