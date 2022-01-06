import sys
import heapq
inputs = sys.stdin.readline
t = int(inputs())
i = [int(inputs()) for i in range(t)]
if t ==1:
  print(0)
else:
  i.sort()a
  a= 0
  c=0
  while not(c >= t-1):
    temp_1 = heapq.heappop(i)
    temp_2 = heapq.heappop(i)
    a+=temp_1+temp_2
    heapq.heappush(i, temp_1 + temp_2)

    c+=1
  print(a) 
