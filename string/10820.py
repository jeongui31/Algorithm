import sys

while True:
    string = sys.stdin.readline().rstrip('\n')
    if not string:
        break
    result = [0]*4
    for s in string:
        if s.islower():
            result[0] += 1
        elif s.isupper():
            result[1] += 1
        elif s.isdigit():
            result[2] += 1
        elif s == ' ':
            result[3] += 1
    print(*result)