import sys
t = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
d = []
e = 1
f = 1


for i in range(1, t):
    if n[i-1] >= n[i]:
        e += 1
    else:
        d.append(e)
        e = 1
    d.append(e)
    if n[i-1] <= n[i]:
        f += 1
    else:
        d.append(f)
        f = 1
    d.append(f)


def Max(a):
    Max = 1
    for i in a:
        if Max < i:
            Max = i
    print(Max)


Max(d)
