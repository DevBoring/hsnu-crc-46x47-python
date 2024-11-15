def hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        print(f"Move disc 1 from {from_pole} to {to_pole}")
        return
    hanoi(n-1, from_pole, aux_pole, to_pole)
    print(f"Move disc {n} from {from_pole} to {to_pole}")
    hanoi(n-1, aux_pole, to_pole, from_pole)

# 測試
hanoi(int(input()), 'A', 'C', 'B')
