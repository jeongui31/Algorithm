from collections import deque
import sys

deque = deque()
N = int(input())
for _ in range(N):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push_front':
        deque.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deque.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if deque :
            n = deque.popleft()
            print(n)
        else :
            print('-1')
    elif cmd[0] == 'pop_back':
        if deque :
            n = deque.pop()
            print(n)
        else :
            print('-1')
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if deque :
            print('0')
        else :
            print('1')
    elif cmd[0] == 'front':
        if deque :
            print(deque[0])
        else :
            print('-1')
    elif cmd[0] == 'back':
        if deque :
            print(deque[-1])
        else :
            print('-1')