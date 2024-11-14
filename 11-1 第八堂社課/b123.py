while True:
    try:
        m, n = map(int, input().split())
        a = []
        mx = 0
        for i in range(m):
            a.append(list(map(int, input().split())))
        for i in range(1, m):
            for j in range(n):
                if a[i][j] == 1:
                    a[i][j] += a[i - 1][j]
        for i in range(m):
            lmin, rmin, sl, sr = [-1] * n, [n] * n, [], []
            for j in range(n):
                while sl and a[i][sl[-1]] >= a[i][j]:
                    sl.pop()
                if sl:
                    lmin[j] = sl[-1]
                sl.append(j)
            for j in range(n - 1, -1, -1):
                while sr and a[i][sr[-1]] >= a[i][j]:
                    sr.pop()
                if sr:
                    rmin[j] = sr[-1]
                sr.append(j)
            for j in range(n):
                mx = max(mx, (rmin[j] - lmin[j] - 1) * a[i][j]);
        print(mx)
    except:
        break