N = int(input())
for i in range(1, N+1):
    for k in range(N-i):
        print("_", end="")
    for j in range(i*2-1):
        print(i, end="")
    print("")
