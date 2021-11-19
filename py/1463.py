import sys
t = int(sys.stdin.readline())
d = [0] * 1000001  # d[n]은 n을 1로 만드는 연산 횟수의 최소값
d[2] = 1
d[3] = 1
for i in range(4, t+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[t])
