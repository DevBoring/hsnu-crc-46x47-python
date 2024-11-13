N = int(input())
a = 1
while N != 1:
    if N%2 == 1:
        N = 3*N + 1
    else:
        N = N//2
    a += 1
print(a)
