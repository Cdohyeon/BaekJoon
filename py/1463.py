import sys
import math
t = int(sys.stdin.readline())
dp = [1, 2, 3]
a = [0, 1, 1, 1, 2, 3, 2, 3, 3, 2, 3]


for i in range(10, t):
    y = i+1
    if y % dp[2] == 0:
        a.append(math.floor(a[dp[2]]+a[y//dp[2]]))
        continue
    if y % dp[1] == 0:
        a.append(math.floor(a[dp[1]]+a[y//dp[1]]))
        continue
    if y % dp[2] != 0 and y % dp[1] != 0:
        count = 0
        while y % dp[2] != 0 and y % dp[1] != 0:
            y -= 1
            count += 1
        if y % dp[2] == 0:
            a.append(math.floor(count+a[dp[2]]+a[y//dp[2]]))
        else:
            a.append(math.floor(count+a[dp[1]]+a[y//dp[1]]))
        continue
print(a[t])
