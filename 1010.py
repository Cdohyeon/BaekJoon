import math
t = int(input())
i = []
e= 0
while t*2 > len(i):
    a, b = map(int, input().split())
    i.append(a)
    i.append(b)
while t*2 > e:
    print(math.floor(math.factorial(i[e+1])/((math.factorial((i[e+1])-i[e]))*math.factorial(i[e]))))
    e+=2