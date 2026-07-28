# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, label="matrix"):
    print(f"Enter {label}:")
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [float(x) for x in row]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        formatted_row = "  ".join(f"{val:g}" for val in row)
        print(formatted_row)


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def main():
    # ----- Part A: Transpose -----
    print("=== Part A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)

    # ----- Part B: Addition -----
    print("\n=== Part B: Add Two Matrices ===")
    print(f"Enter Matrix A ({rows}x{cols}):")
    matrix_a = read_matrix(rows, cols, "Matrix A")
    print(f"Enter Matrix B ({rows}x{cols}):")
    matrix_b = read_matrix(rows, cols, "Matrix B")

    sum_matrix = add_matrices(matrix_a, matrix_b)
    print("\nSum of Matrices:")
    display_matrix(sum_matrix)

    # ----- Part C: Multiplication -----
    print("\n=== Part C: Multiply Two Matrices ===")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A / rows of Matrix B: "))
    p = int(input("Enter columns of Matrix B: "))

    print(f"Enter Matrix A ({m}x{n}):")
    mat_a = read_matrix(m, n, "Matrix A")
    print(f"Enter Matrix B ({n}x{p}):")
    mat_b = read_matrix(n, p, "Matrix B")

    product = multiply_matrices(mat_a, mat_b)
    print("\nProduct of Matrices (A x B):")
    display_matrix(product)


if __name__ == "__main__":
    main()