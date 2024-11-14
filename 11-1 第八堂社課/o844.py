n = int(input())
a = list(map(int, input().split()))
stack = []
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        print(stack[-1] + 1, end = " ")
    else:
        print(0, end = " ")
    stack.append(i)