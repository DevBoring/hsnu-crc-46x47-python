def reverse_string(s):
    for i in range(len(s) - 1, -1, -1):
        print(s[i], end="")
reverse_string(input())