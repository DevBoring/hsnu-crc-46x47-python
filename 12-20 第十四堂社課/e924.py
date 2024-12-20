def is_balanced(s):
    # 定義括號對應的字典
    bracket_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []

    for char in s:
        if char in bracket_map.values():  # 如果是開括號
            stack.append(char)
        elif char in bracket_map.keys():  # 如果是閉括號
            if not stack or stack[-1] != bracket_map[char]:  # 檢查是否匹配
                return 'N'
            stack.pop()  # 匹配成功，彈出堆疊頂部的開括號

    return 'Y' if not stack else 'N'  # 如果堆疊為空，則配對成功


# 主程式
T = int(input())
for _ in range(T):
    s = input().strip()
    print(is_balanced(s))
