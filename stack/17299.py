N = int(input())
A = list(map(int, input().split()))

NGF = [-1] * N
stack = [0]
F = [0] * 1000001

for a in A:
    F[a] += 1


for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)