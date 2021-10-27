
t = int(input())
i = []
z = 0
min = 5
while t*2 > len(i):
    a, b = input().split()
    i.append(a)
    b = int(b)
    i.append(b)


while t*2 > z:
    if min > i[z+1]:
        min = i[z+1]
    z += 2
z = 0
while t*2 > z:
    if min == i[z+1]:
        print(i[z])
    z += 2
