a, b, c = map(int, input().split())
w = b**2 - 4*a*c
if w > 0:
    print("Two different roots x1=", int((-b + w**0.5)/(2*a)) ," , x2=", int((-b - w**0.5)/(2*a)), sep= "")
elif w == 0:
    print("Two same roots x=", int((-b)/(2*a)), sep= "")
else:
    print("No real root")