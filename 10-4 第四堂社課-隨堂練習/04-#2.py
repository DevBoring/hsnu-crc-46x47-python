N = int(input())
R = int(input())
a = 1
for i in range(R):
    a *= (N-i)
print(a)
