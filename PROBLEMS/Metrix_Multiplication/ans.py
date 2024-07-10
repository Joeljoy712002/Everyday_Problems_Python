# multiply metrices

def multiply_matrices(mat1, mat2):
    R1 = len(mat1)
    R2 = len(mat2)
    C1 = len(mat1[0])
    C2 = len(mat2[0])

    # Check if matrices can be multiplied
    if C1 != R2:
        raise ValueError("Cannot multiply matrices: Number of columns in Matrix 1 must be equal to number of rows in Matrix 2")

    # Initialize the result matrix with zeros using list comprehension
    result = [[0] * C2 for _ in range(R1)]

    # Perform matrix multiplication
    for i in range(R1):
        for j in range(C2):
            for k in range(R2):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

def get_matrix_from_user(rows, cols):
    matrix = []
    print(f"Enter the {rows}x{cols} matrix:")

    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)

    return matrix

if __name__ == '__main__':
    try:
        R1 = int(input("Enter the number of rows for Matrix 1: "))
        C1 = int(input("Enter the number of columns for Matrix 1: "))
        R2 = int(input("Enter the number of rows for Matrix 2: "))
        C2 = int(input("Enter the number of columns for Matrix 2: "))

        print("\nEnter Matrix 1:")
        mat1 = get_matrix_from_user(R1, C1)

        print("\nEnter Matrix 2:")
        mat2 = get_matrix_from_user(R2, C2)

        # Multiply matrices
        result = multiply_matrices(mat1, mat2)

        # Print multiplication result
        print("\nMultiplication of given two matrices is:")
        for row in result:
            print(' '.join(map(str, row)))

    except ValueError as e:
        print(e)
