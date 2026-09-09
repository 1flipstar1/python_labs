
e = input().strip()
s = next(i for i in range(len(e)) if e[i].isupper())
d = next(i for i in range(s + 1, len(e)) if e[i].isdigit())
k = d - s + 1

z = []
i = s
while i < len(e):
    z.append(e[i])
    if e[i] == ".":
        break
    i += k
print("".join(z))
