def is_balanced(s):
    # 定義每種括號對應的數字
    bracket_map = {'(': 2, ')': -2, '{': 3, '}': -3, '[': 4, ']': -4, '<': 5, '>': -5}
    balance = 0
    stack = []  # 使用堆疊來檢查配對

    for char in s:
        if char in bracket_map:
            balance += bracket_map[char]
            # 如果是開括號，將其推入堆疊
            if char in ['(', '{', '[', '<']:
                stack.append(char)
            else:
                # 如果是閉括號，檢查堆疊是否有對應的開括號
                if not stack or (char == ')' and stack[-1] != '(') or \
                               (char == '}' and stack[-1] != '{') or \
                               (char == ']' and stack[-1] != '[') or \
                               (char == '>' and stack[-1] != '<'):
                    return 'N'
                stack.pop()  # 配對成功，彈出堆疊頂部的開括號

    # 如果 balance 為 0 且堆疊為空，則配對成功
    return 'Y' if balance == 0 and not stack else 'N'

# 主程式
T = int(input())
results = []

for _ in range(T):
    s = input().strip()
    results.append(is_balanced(s))

# 輸出結果
for result in results:
    print(result)
