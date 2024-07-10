# sub of two metrices

def subtract_matrices(mat1, mat2):
    # Check if matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]               #rslt = [[0] * C2 for _ in range(R1)]

    # Subtract corresponding elements
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] - mat2[i][j]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_matrix_from_user():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print(f"Enter the {rows}x{cols} matrix:")

    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    try:
        print("Enter Matrix 1:")
        mat1 = get_matrix_from_user()

        print("\nEnter Matrix 2:")
        mat2 = get_matrix_from_user()

        # Subtract matrices
        result = subtract_matrices(mat1, mat2)

        # Print matrices and result
        print("\nMatrix 1:")
        print_matrix(mat1)
        print("\nMatrix 2:")
        print_matrix(mat2)
        print("\nSubtraction Result:")
        print_matrix(result)

    except ValueError as e:
        print(e)