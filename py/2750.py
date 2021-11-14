import sys
t = int(sys.stdin.readline())


i = [int(sys.stdin.readline()) for i in range(t)]
i.sort()
for a in range(t):
    print(i[a])
