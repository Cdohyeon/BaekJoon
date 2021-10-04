import math

a = int(input())
b = int(input())

c = a*(b % 10)
d = a*(math.floor((b % 100)/10))
e = a*(math.floor(b/100))

print(c)
print(d)
print(e)
print(c+(d*10)+(e*100))
