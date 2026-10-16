import argparse

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n


def print_table(rows):
    """Печатаем таблицу с шириной столбцов по содержимому."""
    word_width = len("Слово")
    count_width = len("Количество")
    for word, count in rows:
        word_width = max(word_width, len(word))
        count_width = max(count_width, len(str(count)))

    print(f"{'Слово':<{word_width}} | {'Количество':>{count_width}}")
    print(f"{'-' * word_width}-+-{'-' * count_width}")
    for word, count in rows:
        print(f"{word:<{word_width}} | {count:>{count_width}}")


def main():
    """Читаем один файл, сохраняем отчёт и выводим статистику."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", default="data/lab04/input.txt")
    parser.add_argument("--out", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    parser.add_argument("--table", action="store_true")
    args = parser.parse_args()

    text = read_text(args.input_path, args.encoding)
    freq = count_freq(tokenize(normalize(text)))
    rows = top_n(freq, len(freq))
    write_csv(rows, args.out, header=("word", "count"))

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq):
        print(f"{word}:{count}")

    if args.table:
        print()
        print_table(rows)


if __name__ == "__main__":
    main()
