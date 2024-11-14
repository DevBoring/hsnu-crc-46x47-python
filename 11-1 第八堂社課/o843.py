n, i, cnt = int(input()), 5, 0
while i <= n:
    cnt += n // i
    i *= 5
print(cnt)