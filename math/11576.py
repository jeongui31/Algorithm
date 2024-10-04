A, B = map(int, input().split())
m_num = int(input())
M = list(input().split())
A_to_10 = 0
A_to_B = []

for idx, i in enumerate(M[::-1]):
	A_to_10 += A ** idx * int(i)

while A_to_10 :
    A_to_B.append(A_to_10 % B)
    A_to_10 //= B
    
print(" ".join(map(str, A_to_B[::-1])))