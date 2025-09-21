import random

def generate_matrix(rows: int, cols: int, low: int, high: int):
    """Создать матрицу rows×cols со случайными целыми в [low, high] (через циклы)."""
    m = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(low, high))
        m.append(row)
    return m

def add_matrices(A, B):
    """Сложить матрицы одинаковой размерности (через циклы). Вернуть C = A + B."""
    if not A or not B:
        raise ValueError("Матрицы не должны быть пустыми")
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Размерности матриц должны совпадать")
    rows, cols = len(A), len(A[0])

    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def pretty_print_matrix(M, title=None):
    """Аккуратно распечатать матрицу как в примере."""
    if title:
        print(title)
    print("[")
    for i, row in enumerate(M):
        print(" ", row, "," if i < len(M) - 1 else "")
    print("]")

rows = int(input("Введите количество строк (rows): ").strip())
cols = int(input("Введите количество столбцов (cols): ").strip())
rng = input("Введите диапазон значений для элементов (min max), можно отрицательные: ").split()
low, high = map(int, rng)

if rows <= 0 or cols <= 0:
    print("Ошибка: размеры матриц должны быть положительными.")
    raise SystemExit
if low > high:
    low, high = high, low

matrix_1 = generate_matrix(rows, cols, low, high)
matrix_2 = generate_matrix(rows, cols, low, high)
matrix_3 = add_matrices(matrix_1, matrix_2)

pretty_print_matrix(matrix_1, "matrix_1 =")
pretty_print_matrix(matrix_2, "matrix_2 =")
pretty_print_matrix(matrix_3, "matrix_3 = matrix_1 + matrix_2")
