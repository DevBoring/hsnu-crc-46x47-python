ind = [1, 10, 19, 28, 37, 46, 55, 64, 39, 73, 82, 2, 11, 20, 48, 29, 38, 47, 56, 65, 74, 83, 21, 3, 12, 30]
s = input()
check = 0
check += ind[ord(s[0]) - ord('A')]
for i in range(1, 9):
    check += (9 - i) * int(s[i])
check += int(s[9])
if check % 10 == 0:
    print("real")
else:
    print("fake")