n = int(input())
main_list = []
sub_list = []
for i in range(1, n+2):
    sub_list = [i, n-i+1]
    main_list.append(sub_list) #做出二維陣列

def f(h):
    def transform(x, y):
        return [x * y, y - 1]
    return transform
print(main_list)
for row in main_list:
    row[0], row[1] = f(row[1])(row[0], row[1])
print(main_list)