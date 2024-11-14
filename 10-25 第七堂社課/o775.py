row, column = map(int, input().split())
list1=[]
for i in range(row):
    list2=list(map(int,input().split()))
    list1.append(list2)
for i in range(column):
    for j in range(row):
        print(list1[j][i],end=" ")
    print()