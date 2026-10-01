def format_record(rec: tuple[str, str, float]):
    if not isinstance(rec, tuple):  # Проверяем тип записи
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:  # В записи три поля
        raise ValueError("В записи должно быть три поля")
    fio, grp, gpa = rec  # Разбираем кортеж
    if not isinstance(fio, str) or not isinstance(grp, str):
        raise TypeError("ФИО и группа должны быть строками")
    if type(gpa) not in (int, float):
        raise TypeError("GPA должен быть числом")

    p = fio.split()  # Разделяем ФИО без лишних пробелов
    grp = " ".join(grp.split())  # Убираем лишние пробелы
    if len(p) not in (2, 3) or not grp:  # Проверяем ФИО и группу
        raise ValueError("Нужны фамилия, имя и непустая группа")
    if not 0 <= gpa <= 5:  # Проверяем диапазон среднего балла
        raise ValueError("GPA должен быть от 0 до 5")

    ini = ""
    for name in p[1:]:  # Собираем инициалы
        ini += name[0].upper() + "."  # Заглавная буква и точка
    return f"{p[0].capitalize()} {ini}, гр. {grp}, GPA {gpa:.2f}"


for rec in (
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    ("", "BIVT-25", 4.6),
    ("Иванов Иван", "", 4.6),
    ("Иванов Иван", "BIVT-25", "4.6"),
    ("Иванов Иван", "BIVT-25", 5.1),
):
    try:
        print(f"{rec} -> {format_record(rec)}")
    except (ValueError, TypeError) as err:
        print(f"{rec} -> {type(err).__name__}: {err}")
