class Sequence:
    def __init__(self, initial_sequence):
        self.current_sequence = initial_sequence
        self.history = [initial_sequence[:]]  # Initialize history with the initial sequence
        self.ans = 0

    def apply_operation(self, operation):
        op_type = operation[0]
        if op_type == 0:
            k = operation[1]
            self.current_sequence = self.history[k-1][:]
        elif op_type == 1:
            x = operation[1]
            v = operation[2]
            self.current_sequence.insert(x, v)
        elif op_type == 2:
            x = operation[1]
            if 1 <= x <= len(self.current_sequence):
                self.current_sequence.pop(x - 1)
        elif op_type == 3:
            x = operation[1]
            y = operation[2]
            self.current_sequence[x - 1:y] = reversed(self.current_sequence[x - 1:y])
        elif op_type == 4:
            x = operation[1]
            y = operation[2]
            v = operation[3]
            for i in range(x - 1, y):
                self.current_sequence[i] += v
        elif op_type == 5:
            self.history.append(self.current_sequence[:])
            x = operation[1]
            y = operation[2]
            self.ans = max(self.current_sequence[x - 1:y])
            return self.ans
        elif op_type == 6:
            self.history.append(self.current_sequence[:])
            x = operation[1]
            y = operation[2]
            self.ans = min(self.current_sequence[x - 1:y])
            return self.ans
        elif op_type == 7:
            self.history.append(self.current_sequence[:])
            x = operation[1]
            y = operation[2]
            self.ans = sum(self.current_sequence[x - 1:y])
            return self.ans
        self.history.append(self.current_sequence[:])
        print(len(self.history))
        print(len(self.current_sequence))
        return None  # Explicitly return None if no result is produced

# Main execution
n = int(input())
initial_sequence = list(map(int, input().split()))
q = int(input())

results = []
sequence = Sequence(initial_sequence)  # Create an instance of Sequence

for days in range(1, q + 1):
    in_op = list(map(int, input().split()))
    # Decrypt operation
    if sequence.ans == 0:
        operation = in_op
    else:
        operation = [x ^ sequence.ans for x in in_op]
    print(operation)
    result = sequence.apply_operation(operation)  # Call the method on the instance
    if result is not None:
        results.append(result)

# Optionally print results
print("\n".join(map(str, results)))