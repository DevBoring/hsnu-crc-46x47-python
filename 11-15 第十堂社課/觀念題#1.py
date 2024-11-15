def f(i):
    if i > 0:
        if (i // 2) % 2 == 0:
            return f(i - 2) * i
        else:
            return f(i - 2) * (-i)
    else:
        return 1