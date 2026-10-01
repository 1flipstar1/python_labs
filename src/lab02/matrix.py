def transpose(mat: list[list[float | int]]):
    if not mat:  # Проверяем пустую матрицу
        return []
    for row in mat:
        if len(row) != len(mat[0]):  # Проверяем длину строк
            raise ValueError("Строки разной длины")

    res = []
    for j in range(len(mat[0])):  # Столбцы становятся строками
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])  # Берём элемент столбца
        res.append(row)
    return res


def row_sums(mat: list[list[float | int]]):
    if not mat:  # Проверяем пустую матрицу
        return []
    res = []
    for row in mat:
        if len(row) != len(mat[0]):  # Проверяем длину строк
            raise ValueError("Строки разной длины")
        res.append(sum(row))  # Сумма строки
    return res


def col_sums(mat: list[list[float | int]]):
    res = []
    for col in transpose(mat):  # Получаем столбцы как строки
        res.append(sum(col))  # Сумма столбца
    return res


for mat in ([[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]):
    try:
        print(f"transpose({mat}) -> {transpose(mat)}")
    except ValueError as err:
        print(f"transpose({mat}) -> ValueError: {err}")

for mat in ([[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]):
    try:
        print(f"row_sums({mat}) -> {row_sums(mat)}")
    except ValueError as err:
        print(f"row_sums({mat}) -> ValueError: {err}")
    try:
        print(f"col_sums({mat}) -> {col_sums(mat)}")
    except ValueError as err:
        print(f"col_sums({mat}) -> ValueError: {err}")
