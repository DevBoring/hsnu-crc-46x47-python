x = int(input())
y = int(input())
k = int(input())
if x%k == 0:
    xmove = x//k
else:
    xmove = x//k +1
if y % k == 0:
    ymove = y // k
else:
    ymove = y // k + 1

if xmove < ymove:
    xmove = ymove
if xmove > ymove + 1:
    ymove = xmove - 1

print(xmove+ymove)