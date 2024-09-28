n = list(input())
res = []

if len(n) % 3 != 0:
    n = [0] * (3-(len(n)%3)) + n
    
for i in range(0, len(n), 3):
    res.append(int(n[i])*4 + int(n[i+1])*2 + int(n[i+2])*1)
    
for _ in res:
    print(_,end="")