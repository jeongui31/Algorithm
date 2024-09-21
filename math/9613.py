from math import gcd

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    total = 0
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            total += gcd(nums[i], nums[j])
    print(total)