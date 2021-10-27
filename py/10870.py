t = int(input())
i = [0, 1]
while t+2 > len(i):
    i.append(i[len(i)-2] + i[len(i)-1])
print(i[t])
