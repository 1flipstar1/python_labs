import sys

from src.lib.text import normalize, tokenize, count_freq, top_n


text = sys.stdin.read()  # Читаем весь текст до конца ввода
words = tokenize(normalize(text))
freq = count_freq(words)

print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, n in top_n(freq):  # Печатаем слова по частоте
    print(f"{word}:{n}")
