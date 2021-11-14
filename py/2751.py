import sys
t = int(sys.stdin.readline())


i = [int(sys.stdin.readline()) for i in range(t)]
i.sort(reverse=False)
for a in range(t):
    print(i[a])
