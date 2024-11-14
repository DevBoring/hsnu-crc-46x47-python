while True:
    n = int(input())
    if n == 0:
        break
    while True:
        a = list(map(int, input().split()))
        if a[0] == 0:
            break
        cur = 0
        stack = []
        for i in range(1, n + 1):
            stack.append(i)
            while stack and stack[-1] == a[cur]:
                stack.pop()
                cur += 1
        if not stack:
            print("Yes")
        else:
            print("No")
    print()