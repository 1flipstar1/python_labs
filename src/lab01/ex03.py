p = float(input("Цена: ").replace(",", "."))
d = float(input("Скидка (%): ").replace(",", "."))
v = float(input("НДС (%): ").replace(",", "."))
b = p * (1 - d / 100)
vat = b * v / 100
t = b + vat
print(f"База после скидки: {b:.2f} ₽")
print(f"НДС:               {vat:.2f} ₽")
print(f"Итого к оплате:    {t:.2f} ₽")
