def min_max(nums: list[float | int]):
    if not nums:  # Проверяем пустой список
        raise ValueError("Список пуст")

    mn = nums[0]  # Начинаем с первого числа
    mx = nums[0]
    for n in nums:  # Ищем минимум и максимум
        if n < mn:
            mn = n
        if n > mx:
            mx = n
    return mn, mx


def unique_sorted(nums: list[float | int]):
    res = []
    for n in nums:
        if n not in res:  # Пропускаем повторы
            res.append(n)

    for i in range(len(res) - 1):  # Сортировка пузырьком
        for j in range(len(res) - 1 - i):
            if res[j] > res[j + 1]:  # Сравниваем соседние числа
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


def flatten(mat: list[list | tuple]):
    res = []
    for row in mat:
        if not isinstance(row, (list, tuple)):  # Проверяем тип строки
            raise TypeError("Строка должна быть списком или кортежем")
        res.extend(row)  # Добавляем элементы строки
    return res


for nums in ([3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]):
    try:
        print(f"min_max({nums}) -> {min_max(nums)}")
    except ValueError as err:
        print(f"min_max({nums}) -> ValueError: {err}")

for nums in ([3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]):
    print(f"unique_sorted({nums}) -> {unique_sorted(nums)}")

for mat in ([[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]):
    try:
        print(f"flatten({mat}) -> {flatten(mat)}")
    except TypeError as err:
        print(f"flatten({mat}) -> TypeError: {err}")
