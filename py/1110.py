n = int(input())
import math
a = math.floor(n/10)
b = math.floor(n%10)
d , f = a, b
t = a+b
c =0
while 1:

  a = b
  b = math.floor(t%10)
  t = a+b
  
  
  c+=1
  if d == a and f == b:
    break
  
print(c)
