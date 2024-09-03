import sys
word1 = list(sys.stdin.readline().strip())
word2 = []
M = int(input())

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L' and word1 :
        word2.append(word1.pop())
    elif command[0] == 'D' and word2 :
        word1.append(word2.pop())
    elif command[0] == 'B' and word1 :
        word1.pop()
    elif command[0] == 'P':
        word1.append(command[1])
        
answer = word1+word2[::-1]
print(''.join(answer))