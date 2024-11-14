n = int(input())
stack = []
for i in range(n):
    e = input()
    if e.startswith("1"):
        _, x = e.split()
        stack.append(x)
    elif e.startswith("2"):
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        if stack:
            stack.pop()