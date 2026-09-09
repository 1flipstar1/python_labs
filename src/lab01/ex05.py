n = input("ФИО: ")
p = n.split()
i = "".join(x[0] for x in p).upper() + "."
n = " ".join(p)
print(f"Инициалы: {i}")
print(f"Длина (символов): {len(n)}")
