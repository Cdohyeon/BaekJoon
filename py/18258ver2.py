import sys
from collections import deque
t = int(sys.stdin.readline())
b = deque([])
for i in range(t):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        b.append(s[1])
    elif s[0] == 'pop':
        if not b:
            print(-1)
        else:
             print(b.popleft())
    elif s[0] == 'size':
        print(len(b))
    elif s[0] == 'empty':
        if not b:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not b:
            print(-1)
        else:
            print(b[0])
    elif s[0] == 'back':
        if not b:
            print(-1)
        else:
            print(b[-1])
