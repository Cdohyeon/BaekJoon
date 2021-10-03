x, y, w, h = map(int, input().split())

up1 = x
up2 = y

down1 = x
down2 = y

max = 0
min = 0


while up1 < w and up2 < h:
    up1 += 1
    up2 += 1
    max += 1
while down1 > 0 and down2 > 0:
    down1 -= 1
    down2 -= 1
    min += 1

if max > min:
    print(min)
else:
    print(max)
