def calculate_average(args):
    if not args:
        return 0
    return sum(args) // len(args)
try:
    while 1:
        numbers = list(map(int, input().split()))
        print(calculate_average(numbers))
except EOFError:
    None