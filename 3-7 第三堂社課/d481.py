def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

while True:
    try:
        # Read dimensions
        a, b, c, d = map(int, input().split())
        
        # Check if matrices can be multiplied (columns of first = rows of second)
        if b != c:
            print("Error")
            continue
            
        # Read first matrix (a x b)
        matrix1 = []
        for _ in range(a):
            row = list(map(int, input().split()))
            matrix1.append(row)
            
        # Read second matrix (c x d)
        matrix2 = []
        for _ in range(c):
            row = list(map(int, input().split()))
            matrix2.append(row)
            
        # Perform matrix multiplication
        result = []
        for i in range(a):
            row = []
            for j in range(d):
                sum_val = 0
                for k in range(b):
                    sum_val += matrix1[i][k] * matrix2[k][j]
                row.append(sum_val)
            result.append(row)
            
        # Print result
        print_matrix(result)
        
    except EOFError:
        break
