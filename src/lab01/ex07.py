
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
