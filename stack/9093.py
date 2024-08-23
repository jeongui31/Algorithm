import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sentence = input().split()
    stack = []
    for word in sentence:
        for ch in word:
            stack.append(ch)
        while stack:
            print(stack.pop(), end="")
        print(" ", end="")
    print()