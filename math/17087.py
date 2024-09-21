from math import gcd
from functools import reduce

N, S = map(int, input().split())
A = list(map(int, input().split()))
A = [abs(a-S) for a in A]

print(reduce(gcd, A))