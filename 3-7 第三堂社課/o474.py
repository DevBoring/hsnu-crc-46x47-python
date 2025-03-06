#input
N = int(input())
base = []
exponent = []
for i in range (N+1):
    base_in, exponent_in = map(int, input().split())
    base.append(base_in)
    exponent.append(exponent_in)

#微分output
print("a(x)=")
if N == 0:
    print("0 0")
else:
    for j in range (N):
        print(base[j] * exponent[j], exponent[j]-1)

#積分outout
print("A(x)=")
for k in range (N+1):
    print((base[k])//(exponent[k] + 1), exponent[k] + 1)
print("c 0")
