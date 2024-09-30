sosu = [False, False] + [True]*999999

for i in range(2, 1000001):
    if sosu[i]:
        for j in range(i*2, 1000001, i):
            sosu[j] = False

T = int(input())
for _ in range(T):
    count = 0
    num = int(input())
    for n in range(2, num//2+1):
        if sosu[n] and sosu[num-n]:
            count += 1
    print(count)