# Лабораторная работа 1

<details>
<summary>Код заданий 1–7</summary>

### Задание 1

```python
n = input("Имя: ").strip()
a = int(input("Возраст: "))
print(f"Привет, {n}! Через год тебе будет {a + 1}.")
```

### Задание 2

```python
a = float(input("a: ").replace(",", "."))
b = float(input("b: ").replace(",", "."))
s = a + b
print(f"sum={s}; avg={s / 2}")
```

### Задание 3

```python
p = float(input("Цена: ").replace(",", "."))
d = float(input("Скидка (%): ").replace(",", "."))
v = float(input("НДС (%): ").replace(",", "."))
b = p * (1 - d / 100)
vat = b * v / 100
t = b + vat
print(f"База после скидки: {b} ₽")
print(f"НДС:               {vat} ₽")
print(f"Итого к оплате:    {t} ₽")
```

### Задание 4

```python
m = int(input("Минуты: "))
h = m // 60
m = m % 60
print(f"{h}:{m:02d}")
```

### Задание 5

```python
n = input("ФИО: ")
p = n.split()
i = "".join(x[0] for x in p).upper() + "."
n = " ".join(p)
print(f"Инициалы: {i}")
print(f"Длина (символов): {len(n)}")
```

### Задание 6

```python
n = int(input())
a = 0
b = 0
for _ in range(n):
    x = input().split()
    if x[-1] == "True":
        a += 1
    else:
        b += 1
print(a, b)
```

### Задание 7

```python

e = input().strip()
s = 0
for i in range(len(e)):
    if e[i].isupper():
        s = i
        break

d = 0
for i in range(s + 1, len(e)):
    if e[i].isdigit():
        d = i
        break

k = d - s + 1

z = []
i = s
while i < len(e):
    z.append(e[i])
    if e[i] == ".":
        break
    i += k
print("".join(z))
```

</details>


## 1–6 задания

Скриншот выполнения заданий 1–6:

![Скриншот выполнения заданий 1–6](<../../images/lab01/1-6%20ex.png>)

## 7 задание

Скриншот выполнения 7 задания:

![Скриншот выполнения задания 7](<../../images/lab01/7%20ex.png>)