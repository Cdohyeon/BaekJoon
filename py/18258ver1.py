import sys
t = int(sys.stdin.readline())
b = []

for e in range(t):
    i = sys.stdin.readline().split()
    blen = len(b)
    if i[0]=='push':
        b.append(i[1])
    if i[0]=="pop":
        if blen == 0:
            print(-1)
        else:
            print(b[0])
            del b[0]
    if i[0]=="size":
        print(blen)
    if i[0]=="empty":
        if blen == 0:
            print(1)
        else:
            print(0)
    if i[0]=='back':
        if blen == 0:
            print(-1)
        else:
            print(b[blen-1])
    if i[0]=="front":
        if blen == 0:
            print(-1)
        else:
            print(b[0])

