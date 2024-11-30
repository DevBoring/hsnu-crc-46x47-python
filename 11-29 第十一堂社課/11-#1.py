length = int(input())

days = []
ans = 0


def zero(k):
    global process
    process = days[k]


def one(x, v):
    global process
    process.insert(x, v)


def two(x):
    global process
    process.pop(x - 1)


def three(x, y):
    global process
    l = process[:x - 1]
    r = process[y:]
    reversed = process[x - 1:y][::-1]
    process = l + reversed + r


def four(x, y, v):
    global process
    for i in range(x - 1, y):
        process[i] += v


def five(x, y):
    global process
    global ans
    ans = max(process[x - 1:y])
    print(ans)


def six(x, y):
    global process
    global ans
    ans = min(process[x - 1:y])
    print(ans)


def seven(x, y):
    global process
    global ans
    ans = sum(process[x - 1:y])
    print(ans)


process = list(map(int, input().split()))
days.append(process)

day = int(input())
# day = 15

for _ in range(day):
    orig_query = list(map(int, input().split()))
    query = list(map(lambda x: x ^ ans, orig_query))
    # print (query)
    ope = query[0]

    if ope == 0:
        zero(query[1])

    elif ope == 1:
        one(query[1], query[2])

    elif ope == 2:
        two(query[1])

    elif ope == 3:
        three(query[1], query[2])

    elif ope == 4:
        four(query[1], query[2], query[3])

    elif ope == 5:
        five(query[1], query[2])

    elif ope == 6:
        six(query[1], query[2])

    elif ope == 7:
        seven(query[1], query[2])

    # print(process)
    days.append(process)