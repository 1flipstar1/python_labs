import re


def normalize(text, *, casefold=True, yo2e=True):
    if casefold:  # Приводим текст к нижнему регистру
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:  # Объединяем слова с ё и е
        text = text.replace("ё", "е")

    return " ".join(text.split())  # Убираем лишние пробелы и переносы


def tokenize(text):
    return re.findall(r"\w+(?:-\w+)*", text)  # Сохраняем дефис внутри слова


def count_freq(tokens):
    res = {}
    for word in tokens:  # Считаем каждое слово
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


def top_n(freq, n=5):
    if n < 0:
        raise ValueError("Количество слов не может быть отрицательным")

    res = sorted(freq.items(), key=lambda p: (-p[1], p[0]))
    return res[:n]
