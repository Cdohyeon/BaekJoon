import sys
t = int(sys.stdin.readline())
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(1, t+1):
    y = int(sys.stdin.readline())
    for e in range(4, y+1):
        d[e] = d[e-1]
        d[e] += d[e-2]
        d[e] += d[e-3]
    print(d[y])
