import sys

t = int(sys.stdin.readline())
b = []
    
i = [sys.stdin.readline().strip() for i in range(t)]


for e in i:
    blen = len(b)
    if e.find("push") != -1:
        f = []
        d = 5
        g = list(str(e))
        while len(g) > d:
            f.append(g[d])
            d += 1
        b.append(''.join(f))
        
    if e.find("pop") != -1:
        if blen == 0:
            print(-1)
        else:
            print(b[blen-1])
            del b[blen-1]
    if e.find("size") != -1:
        print(blen)
    if e.find("empty") != -1:
        if blen == 0:
            print(1)
        else:
            print(0)
    if e.find("top") != -1:
        if blen == 0:
            print(-1)
        else:
            print(b[blen-1])

