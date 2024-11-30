import re

def data_field(statement, index):
    if statement[index+1] != '=':
        return -1

    value = 0
    index += 2
    while index < len(statement) and statement[index].isdigit():
        value = value * 10 + int(statement[index])
        index += 1

    if index < len(statement) and statement[index] == '.':
        position = 0.1
        index += 1
        while index < len(statement) and statement[index].isdigit():
            value += (ord(statement[index]) - ord('0')) * position
            position *= 0.1
            index += 1

    # Prefix Check
    if index < len(statement) and statement[index] == 'm':
        value *= 1e-3
        index += 1
    elif index < len(statement) and statement[index] == 'k':
        value *= 1e3
        index += 1
    elif index < len(statement) and statement[index] == 'M':
        value *= 1e6
        index += 1

    # Unit
    if index < len(statement) and (statement[index] == 'W' or statement[index] == 'V' or statement[index] == 'A'):
        return value
    else:
        return -1

def main():
    num_testcase = int(input())
    for testcase in range(1, num_testcase+1):
        statement = input()

        value = [-1, -1, -1]
        for i in range(len(statement)):
            if statement[i] == 'P':
                value[0] = data_field(statement, i)
            elif statement[i] == 'U':
                value[1] = data_field(statement, i)
            elif statement[i] == 'I':
                value[2] = data_field(statement, i)

        print(f"Problem #{testcase}")
        if value[0] == -1:
            print(f"P={value[1]*value[2]:.2f}W")
        elif value[1] == -1:
            print(f"U={value[0]/value[2]:.2f}V")
        elif value[2] == -1:
            print(f"I={value[0]/value[1]:.2f}A")
        print()

if __name__ == "__main__":
    main()