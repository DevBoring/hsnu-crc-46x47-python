N, T = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

AND = []
OR = []
XOR = []
for i in range(T):
    ones = 0
    for j in range(N):
        ones += (a[j][i] == 1)
    if ones == N:
        AND.append(1)
    else:
        AND.append(0)
    if ones >= 1:
        OR.append(1)
    else:
        OR.append(0)
    if ones % 2:
        XOR.append(1)
    else:
        XOR.append(0)

print("AND:", end='')
for i in range(T):
    print(" ", AND[i], sep='', end='')
print()

print(" OR:", end='')
for i in range(T):
    print(" ", OR[i], sep='', end='')
print()

print("XOR:", end='')
for i in range(T):
    print(" ", XOR[i], sep='', end='')
print()
