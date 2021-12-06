import sys
a = [0] * 5
a[1] = (1, 0, 0)
a[2] = (0, 1, 0)
a[3] = (1, 1, 1)
a[4] = (2, 0, 1)

app = a.append

max = 100001
mod = 1000000009


for e in range(5, max):
    app(((a[e-1][1]+a[e-1][2]) % mod, (a[e-2][0] + a[e-2][2]) %
        mod, (a[e-3][0]+a[e-3][1]) % mod))

t = int(sys.stdin.readline())

for i in range(t):
    g = int(sys.stdin.readline())
    print(sum(a[g]) % mod)
