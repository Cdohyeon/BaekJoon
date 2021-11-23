import sys
t = int(sys.stdin.readline())

a = [[1]]
count = 0
for i in range(1, t + 1):
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 1:
        n[2] = n[2]-1
        if n[2] == 0:
            count += n[1]
        else:
            a.append(n)
    else:
        if len(a) == 1:
            continue
        a[len(a)-1][2] = a[len(a)-1][2] - 1
        if a[len(a)-1][2] == 0:
            count += a[len(a)-1][1]
            a.pop()
print(count)
