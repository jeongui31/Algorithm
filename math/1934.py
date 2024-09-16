import sys

T = int(input())

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

for _ in range(T):
    S = list(map(int, sys.stdin.readline().split()))
    print(lcm(S[0], S[1]))