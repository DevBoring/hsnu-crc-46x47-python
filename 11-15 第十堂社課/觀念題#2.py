def f(n):
    if n > 3:
        return 1
    elif n == 2:
        return 3 + f(n + 1)
    else:
        return 1 + f(n + 1)

def g(n):
    j = 0
    for i in range(1, n):
        j += f(i)
    return j
